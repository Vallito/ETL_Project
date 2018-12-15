import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pymysql
from flask import Flask, jsonify, render_template

# Connect to database

engine = create_engine("mysql://root:Valls.1992@localhost/trees_db")

# Set automap
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#save table to variable
tree_table = Base.classes.nyc_trees

session = Session(engine)

# Flask Setup

app = Flask(__name__)

# Flask Routes

@app.route("/")
def main():
    data = session.query(tree_table).all()
   

    # Convert list of tuples into normal list
    all_trees = []
    for tree_type in data:
        tree_dict = {}
        tree_dict['species_nm'] = tree_type.species_nm
        tree_dict['zip_code'] = tree_type.zip_code
        tree_dict['count_tree'] = tree_type.count_tree
        tree_dict['avg_diameter'] = tree_type.avg_diameter
        all_trees.append(tree_dict)
    return jsonify(all_trees)

@app.route("/web")
def site():
    main_table = list(session.query(tree_table).all())
    return render_template("index.html", tree = main_table)

if __name__ == '__main__':
    app.run(debug=True)
