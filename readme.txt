
C:\Users\dminik\Documents\6.Финальный проект\dminik6_w3.ipynb

Первый вариант (заменен на более короткий через while)
def prepare_train_set_with_fe(path_to_csv_files, site_freq_path, feature_names,
                                    session_length=10, window_size=10):
    with open(site_freq_path, 'rb') as f:
        countdict = pickle.load(f)
    
    files = glob(os.path.join(path_to_csv_files, 'user????.csv'))
    lOut = []

    for fname in files:
        user_id = int(fname[-8:-4])
        l, t = [], []
        with open(fname) as f:                        
            for line in [line.rstrip() for line in f][1:]:
                atmp = line.split(',')
                l.append(countdict[atmp[1]][0])
                t.append(datetime.strptime(atmp[0], "%Y-%m-%d %H:%M:%S"))
                
        numses = (len(l)//window_size)
        if numses*window_size == len(l): numses-=1
        nadd = ((numses * window_size + session_length) - len(l))# %session_length
        if nadd != 0: l += list(np.zeros(nadd, dtype=np.int))
         
        lenmax = len(l)
        for i in np.arange(0, numses+1, dtype=np.int):
            ldattmp = t[i*window_size: min(i*window_size + session_length, lenmax)]
            dmin = min(ldattmp)
            ltmp = l[i*window_size: min(i*window_size + session_length, lenmax)]
            lOut += [ ltmp +  [ 0, 0, 0, 0, 0, 0, 0, 0, 0] + 
                     [(max(ldattmp) - dmin).total_seconds(), 
                      len(set(ltmp).difference([0])), 
                      dmin.hour, dmin.weekday(), user_id] ]
              
    
    dfOut = pd.DataFrame( lOut, columns= feature_names, dtype=np.int)
    
    return dfOut