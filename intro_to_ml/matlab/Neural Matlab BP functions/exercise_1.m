input=0.7
Wout=0.8
Whid=0.4
T=1
SUMhid=input*Whid
Ahid=sigmoid (SUMhid)
SUMout=Ahid*Wout
Aout=purelin(SUMout)
DELTAout=(T-Aout)*dpurelin(Aout)
DELTAhid=DELTAout*Wout*dsigmoid(SUMhid)
Wout=Wout+DELTAout*Ahid
Whid-Whid+DELTAhid*input
purelin((sigmoid(input *Whid)) *Wout)