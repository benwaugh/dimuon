from dimuon import find_pairs
from nose.tools import *

def test_no_particles():
    particles = []
    pairs = find_pairs(particles)
    assert len(pairs) == 0

def test_one_particle():
    particles = [None]
    pairs = find_pairs(particles)
    assert len(pairs) == 0

def test_two_particles():
    particles = [None,None]
    pairs = find_pairs(particles)
    assert_equal(len(pairs), 1)
