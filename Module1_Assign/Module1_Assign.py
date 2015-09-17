import matplotlib.pyplot as pst
import Degrees_distribution as dg
import import_script as isi
import numpy as np
cit_dict = isi.load_graph(isi.CITATION_URL)
cita_distrib = dg.normalized_distribution(cit_dict)
#cita_distrib = dg.normalized_distribution(dg.EX_GRAPH0)
#pst.subplots_adjust(hspace=0.4)

axe_x = [key for key in sorted(cita_distrib)]
axe_y = [value for dummy_key,value in cita_distrib.iteritems()]
pst.xlabel("Number of edges")
pst.ylabel("Normalized occurence")


pst.grid(True)
pst.title('loglog base of Normalized distribution per number of edges')
axe_y = pst.gca()
axe_y.invert_yaxis()
pst.loglog(axe_y, axe_x)
pst.show()
