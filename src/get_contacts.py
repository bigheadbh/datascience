#!/usr/bin/env python

import sys
import numpy as np
from scipy import spatial
import mmap
from collections import defaultdict
from timeit import default_timer as timer
import pickle

def load_points(name_file, points, info):
    info = []
    points = []
    with open(name_file, "r") as in_file:
        mm = mmap.mmap(in_file.fileno(),0)
    while True:
        line = mm.readline()
        if line == "": break
        line = line[:-1]
        splitted_line = line.split(' ')
        obj_ID = splitted_line[1]
        time = splitted_line[0]
        x = splitted_line[2]
        y = splitted_line[3]
        speed = splitted_line[4]
        points.append((float(x),float(y)))
        info.append((str(obj_ID), float(time), float(speed)))
    mm.close()

def create_kdtree(points, info, contacts):
    tree = spatial.KDTree(points)
    points = []
    contacts = defaultdict(set)
    
    point_index = 0
    for point in tree.data:
        neighbors = tree.query_ball_point(point, 100)
        for neighbor in neighbors:
            info_i = info[point_index]
            info_j = info[neighbor]
            time_i = info_i[1]
            time_j = info_j[1]
            id_i = info_i[0]
            id_j = info_j[0]
            x_i = tree.data[point_index][0]
            y_i = tree.data[point_index][1]
            x_j = tree.data[neighbor][0]
            y_j = tree.data[neighbor][1]

            # Houve um contato
            if time_j == time_i:
                time_contact = time_i
                id_i_N = int("".join(str(ord(c)) for c in id_i))
                id_j_N = int("".join(str(ord(c)) for c in id_j))
                if id_i != id_j:
                    if id_i_N > id_j_N:
                        contacts[(id_i, id_j)].add((time_contact, (x_i, y_i), (x_j, y_j)))
                    if id_i_N < id_j_N:
                        contacts[(id_j, id_i)].add((time_contact, (x_j, y_j), (x_i, y_i)))
                    if id_i_N == id_j_N:
                        print ("ASCII Conflict")
        point_index = point_index + 1

def save_file(name_file, contacts):
    out_file = open(name_file, 'wb')
    pickle.dump(contacts, out_file)
    out_file.close()
