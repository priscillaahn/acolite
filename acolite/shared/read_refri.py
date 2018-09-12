## load WOPP refractive index of water for 27°C and 0 PSU
## QV 2018-07-30

def read_refri():
    import acolite as ac

    file = '{}/{}'.format(ac.config['pp_data_dir'], 'Shared/WOPP/computed_refri_T27_S0.dat')

    data = {'wave':[], 'n':[]}
    with open(file, 'r') as f:
        for line in f.readlines():
            if line[0] in ['%', '#', ';']: continue
            line = line.strip()
            s = line.split()
            if len(s) == 2:
                data['wave'].append(float(s[0]))
                data['n'].append(float(s[1]))
    return(data)