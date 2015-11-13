from dimuon import find_pairs
from nose.tools import *

class DummyParticle:
    def __init__(self, qpt):
        self.qpt = qpt

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
    assert_equal(len(pairs), 1)

def test_two_particles_like_sign():
    pos1 = DummyParticle(+1)
    pos2 = DummyParticle(+1)
    particles = [pos1,pos2]
    pairs = find_pairs(particles)
    assert_equal(len(pairs), 0)
