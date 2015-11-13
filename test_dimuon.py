from dimuon import find_pairs

def test_find_pairs():
    particles = None
    pairs = find_pairs(particles)

def test_no_particles():
    particles = []
    pairs = find_pairs(particles)
    assert len(pairs) == 0

def test_one_particle():
    particles = [None]
    pairs = find_pairs(particles)
    assert len(pairs) == 0
