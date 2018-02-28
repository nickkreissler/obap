from data.playersdata import players as a
y=['GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB', 'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']

GP ={}
MPG={}
FGM={}
FGA={}
FG={}
PM={}
PA={}
P={}
FTM={}
FTA={}
FT={}
TOV={}
PF={}
ORB={}
DRB={}
RPG={}
APG={}
SPG={}
BPG={}
PPG={}

for i in a:
    if float(a[i]['GP']) not in GP.keys():
        GP[float(a[i]['GP'])] = [i]
    else:
        GP[float(a[i]['GP'])] += [i]

    if float(a[i]['MPG']) not in MPG.keys():
        MPG[float(a[i]['MPG'])] = [i]
    else:
        MPG[float(a[i]['MPG'])] += [i]

    if float(a[i]['FGM']) not in FGM.keys():
        FGM[float(a[i]['FGM'])] = [i]
    else:
        FGM[float(a[i]['FGM'])] += [i]

    if float(a[i]['FGA']) not in FGA.keys():
        FGA[float(a[i]['FGA'])] = [i]
    else:
        FGA[float(a[i]['FGA'])] += [i]

    if float(a[i]['FG%']) not in FG.keys():
        FG[float(a[i]['FG%'])] = [i]
    else:
        FG[float(a[i]['FG%'])] += [i]

    if float(a[i]['3PM']) not in PM.keys():
        PM[float(a[i]['3PM'])] = [i]
    else:
        PM[float(a[i]['3PM'])] += [i]

    if float(a[i]['3PA']) not in PA.keys():
        PA[float(a[i]['3PA'])] = [i]
    else:
        PA[float(a[i]['3PA'])] += [i]

    if float(a[i]['3PM']) not in PM.keys():
        PM[float(a[i]['3PM'])] = [i]
    else:
        PM[float(a[i]['3PM'])] += [i]

    if float(a[i]['3P%']) not in P.keys():
        P[float(a[i]['3P%'])] = [i]
    else:
        P[float(a[i]['3P%'])] += [i]

    if float(a[i]['FTM']) not in FTM.keys():
        FTM[float(a[i]['FTM'])] = [i]
    else:
        FTM[float(a[i]['FTM'])] += [i]

    if float(a[i]['FTA']) not in FTA.keys():
        FTA[float(a[i]['FTA'])] = [i]
    else:
        FTA[float(a[i]['FTA'])] += [i]

    if float(a[i]['FT%']) not in FT.keys():
        FT[float(a[i]['FT%'])] = [i]
    else:
        FT[float(a[i]['FT%'])] += [i]

    if float(a[i]['TOV']) not in TOV.keys():
        TOV[float(a[i]['TOV'])] = [i]
    else:
        TOV[float(a[i]['TOV'])] += [i]

    if float(a[i]['PF']) not in PF.keys():
        PF[float(a[i]['PF'])] = [i]
    else:
        PF[float(a[i]['PF'])] += [i]

    if float(a[i]['ORB']) not in ORB.keys():
        ORB[float(a[i]['ORB'])] = [i]
    else:
        ORB[float(a[i]['ORB'])] += [i]

    if float(a[i]['DRB']) not in DRB.keys():
        DRB[float(a[i]['DRB'])] = [i]
    else:
        DRB[float(a[i]['DRB'])] += [i]

    if float(a[i]['RPG']) not in RPG.keys():
        RPG[float(a[i]['RPG'])] = [i]
    else:
        RPG[float(a[i]['RPG'])] += [i]

    if float(a[i]['APG']) not in APG.keys():
        APG[float(a[i]['APG'])] = [i]
    else:
        APG[float(a[i]['APG'])] += [i]

    if float(a[i]['SPG']) not in SPG.keys():
        SPG[float(a[i]['SPG'])] = [i]
    else:
        SPG[float(a[i]['SPG'])] += [i]

    if float(a[i]['BPG']) not in BPG.keys():
        BPG[float(a[i]['BPG'])] = [i]
    else:
        BPG[float(a[i]['BPG'])] += [i]

    if float(a[i]['PPG']) not in PPG.keys():
        PPG[float(a[i]['PPG'])] = [i]
    else:
        PPG[float(a[i]['PPG'])] += [i]


z = open('data/statsdata.py','a+')


z.write('GP ='+str(GP))
z.write('MPG ='+str(MPG))
z.write('FGM ='+str(FGM))
z.write('FGA ='+str(FGA))
z.write('FG ='+str(FG))
z.write('PM ='+str(PM))
z.write('PA ='+str(PA))
z.write('P ='+str(P))
z.write('FTM ='+str(FTM))
z.write('FTA ='+str(FTA))
z.write('FT ='+str(FT))
z.write('TOV ='+str(TOV))
z.write('PF ='+str(PF))
z.write('ORB ='+str(ORB))
z.write('DRB ='+str(DRB))
z.write('RPG ='+str(RPG))
z.write('APG ='+str(APG))
z.write('SPG ='+str(SPG))
z.write('BPG ='+str(BPG))
z.write('PPG ='+str(PPG))


z.close()
