from ROOT import TFile

f = TFile("test_data/events.root")
t = f.Get("events")
n = t.GetEntries()
print "Number of events = " + str(n)

for i in xrange(n):
    t.GetEntry(i)
    n2 = t.nPart
    print "Number of particles = " + str(n2)