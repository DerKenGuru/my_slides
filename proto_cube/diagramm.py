import matplotlib.pyplot as plt
import numpy as np


series = [
    0,0,0,0,0,
    1,1,1,2,2,
    5,5,5,5,2,
    1,1,0,0,0,
    0,0,0,0,0,
    1,2,2,5,5,
    5,5,5,2,2,
    5,5,5,2,1,
    0,0,0,0,0
    ]

plt.step(np.arange(len(series)), series, linewidth=3)
plt.yticks([0,1,2,5], labels=['Aus', 'Standby', 'Leerlauf', 'Bearbeitung'])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off


plt.xlabel("Zeit")
plt.show()
# plt.savefig("matpl.svg", dpi=150)

# graph BT
#     S[Sensoren] --- R[RevPi]
#     W[App-Device] --- |REST, WebSocket| R
#     W --- |REST| A[(Auftragsdatenbank)]
#     R --- I[(InfluxDB)]
#     I --- G[Grafana]