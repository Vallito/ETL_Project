import numpy as np
import sqlalchemy
import pymysql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct

from flask import Flask, jsonify, render_template
from  mysql_scr import pw
# Connect to database

engine = create_engine(f"mysql://root:{pw}@localhost/tree_db")

# Set automap
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#save table to variable
tree_table = Base.classes.nyc_tree
species_table = Base.classes.tree_species

session = Session(engine)

# Flask Setup

app = Flask(__name__)

# Flask Routes

@app.route("/")
def main():
    tree_sq = session.query(species_table.species_nm,species_table.img_loc,tree_table.borough)\
    .filter(species_table.species_nm==tree_table.species_nm,species_table.img_loc.isnot(None)).order_by(func.random()).limit(50).subquery()


    data = session.query(tree_table.borough\
    ,func.sum(tree_table.count_tree).label("total_trees")\
    ,func.count(distinct(tree_table.species_nm)).label("species_count")\
    ,tree_sq.c.img_loc.label("img_loc"))\
    .outerjoin(tree_sq, tree_sq.c.borough  == tree_table.borough)\
    .group_by(tree_table.borough).all()
   
    tree_data = session.query(species_table.species_nm,species_table.img_loc,tree_table.borough)\
    .filter(species_table.species_nm==tree_table.species_nm,species_table.img_loc.isnot(None)).group_by(tree_table.borough,species_table.species_nm).order_by(func.count(species_table.species_nm))
   
    # Convert list of tuples into normal list
    all_boroughs = []
    for borough in data:
        print(borough)
        trees = []
        for tree in tree_data: 
            if tree.borough == borough.borough:
                #print(borough, tree.species_nm)
                trees.append(tree.species_nm.title())
        trees.sort()
        #print(trees)
        borough_dict = {}
        borough_dict['species_count'] = borough.species_count
        borough_dict['borough'] = borough.borough
        borough_dict['total_trees'] = borough.total_trees
        borough_dict['img'] = borough.img_loc
        borough_dict['trees'] = trees
        all_boroughs.append(borough_dict)
    #print(all_boroughs)
    return render_template("index.html", boroughs = all_boroughs)

@app.route("/<tree_name>")
def site(tree_name):
    main_table = list(session.query(species_table.species_nm.label("species_nm")\
    ,species_table.bloom_time
    ,species_table.longevity
    ,species_table.img_loc
    ,species_table.growth_habit).filter(species_table.species_nm == tree_name, species_table.img_loc.isnot(None)))
    return render_template("species.html", trees = main_table)

if __name__ == '__main__':
    app.run(debug=True)
