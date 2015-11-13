#!/bin/env python
#
# Plot dimuon mass distribution for SWC HEP 2015
#
from ROOT import TFile, TH1D

def tree_from_file(path):
    global file_events
    file_events = TFile(path)
    tree_events = file_events.Get("events")
    print type(tree_events)
    return tree_events
    
def dimuon_masses(tree):
    n_events = tree.GetEntries()
    for i_event in xrange(n_events):
        tree.GetEntry(i_event)
        n_particles = tree.nPart
        print "Number of particles = " + str(n_particles)
    h = TH1D("hist_m", "dimuon mass", 100, 0, 200)
    return h

def find_pairs(particles):
    return []

if __name__ == '__main__':
    tree_events = tree_from_file("test_data/events.root")
    print type(tree_events)
    hist_dimuon_mass = dimuon_masses(tree_events)
    hist_dimuon_mass.Draw()
