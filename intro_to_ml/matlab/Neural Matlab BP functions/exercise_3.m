Whid = [0.4, 0.5;
        0.3, 0.2]
Wout = [0.8, 0.7;
        0.6, 0.5] 
input = [0.7, 0.3];
T = [1, 1];

SUMhid = input * Whid
Ahid = sigmoid(SUMhid)
SUMout = Ahid * Wout
Aout = purelin(SUMout)

DELTAhid = [ (DELTAout * Wout(1,:)') * dsigmoid(Ahid(1)), ...
             (DELTAout * Wout(2,:)') * dsigmoid(Ahid(2)) ];

DELTAout = (T - Aout) .* dpurelin(SUMout)
             
Wout = Wout + Ahid' * DELTAout
Whid = Whid + input' * DELTAhid

purelin(sigmoid(input * Whid) * Wout)