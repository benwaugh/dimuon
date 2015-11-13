from ROOT import TFile

f = TFile("test_data/events.root")
t = f.Get("events")
n = t.GetEntries()
print "Number of events = " + str(n)