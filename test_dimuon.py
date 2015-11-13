from dimuon import *
from nose.tools import *
from math import pi

class DummyParticle:
    def __init__(self, q):
        self.q = q

def test_no_particles():
    particles = []
    pairs = find_pairs(particles)
    assert len(pairs) == 0

def test_one_particle():
    pos = DummyParticle(+1)
    particles = [pos]
    pairs = find_pairs(particles)
    assert len(pairs) == 0

def test_two_particles_unlike_sign():
    pos = DummyParticle(+1)
    neg = DummyParticle(-1)
    particles = [pos,neg]
    pairs = find_pairs(particles)
    assert_equal(pairs, [(pos,neg)] )

def test_two_particles_like_sign():
    pos1 = DummyParticle(+1)
    pos2 = DummyParticle(+1)
    particles = [pos1,pos2]
    pairs = find_pairs(particles)
    assert_equal(len(pairs), 0)

def test_inv_mass_zero_mass_particles():
    pos = Particle(1.0, +1.0,  0, pi/2) # massless particle with pt = 1 GeV
    neg = Particle(1.0, -1.0, pi, pi/2) # massless, pt = 1 GeV, opposite direction
    assert_equal(inv_mass_from_pair((pos,neg)), 2.0)

def test_inv_mass_nonzero_mass_particles():
    # shouldn't actually make any difference if masses are non-zero
    pos = Particle(1.0, +0.5,  0, pi/2)
    neg = Particle(1.0, -0.5, pi, pi/2)
    assert_equal(inv_mass_from_pair((pos,neg)), 2.0)

