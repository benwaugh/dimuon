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
    pairs = []
    num_particles = len(particles)
    for i_first in xrange(num_particles):
        for i_second in xrange(i_first+1, num_particles):
            p_first = particles[i_first]
            p_second = particles[i_second]
            if p_first.qpt * p_second.qpt < 0:
                pairs.append( (p_first, p_second) )
    return pairs

if __name__ == '__main__':
    tree_events = tree_from_file("test_data/events.root")
    print type(tree_events)
    hist_dimuon_mass = dimuon_masses(tree_events)
    hist_dimuon_mass.Draw()
