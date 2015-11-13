#!/bin/env python
#
# Plot dimuon mass distribution for SWC HEP 2015
#
from ROOT import TFile, TH1D

class Particle:
    def __init__(self, energy, qpt, phi, theta):
        self.energy = energy
        self.qpt    = qpt
        self.phi    = phi
        self.theta  = theta

def tree_from_file(path):
    global file_events
    file_events = TFile(path)
    tree_events = file_events.Get("events")
    return tree_events
    
def inv_mass_from_pair(pair):
    return 0.0

def dimuon_masses(tree):
    h = TH1D("hist_m", "dimuon mass", 100, 0, 200)
    n_events = tree.GetEntries()
    for i_event in xrange(n_events):
        tree.GetEntry(i_event)
        particles = []
        n_particles = tree.nPart
        for i_particle in xrange(n_particles):
            e = tree.E[i_particle]
            particle = Particle(e, tree.qpt[i_particle], tree.phi[i_particle], tree.theta[i_particle])
            particles.append(particle)
        pairs = find_pairs(particles)
        for pair in pairs:
            m = inv_mass_from_pair(pair)
            h.Fill(m)
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
    hist_dimuon_mass = dimuon_masses(tree_events)
    hist_dimuon_mass.Draw()
