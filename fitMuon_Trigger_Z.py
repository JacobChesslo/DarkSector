import FWCore.ParameterSet.Config as cms
import sys, os, shutil
from optparse import OptionParser

#_*_*_*_*_*_
#Read Inputs
#_*_*_*_*_*_

def FillNumDen(num):
    '''Declares the needed selections for a givent numerator, denominator'''
    process.TnP_Trigger.Variables.mass = cms.vstring("Tag-muon Mass", _mrange, "105", "GeV/c^{2}")

    if num == "TrkMu16NoVtx":
        process.TnP_Trigger.Categories.Control16ByPathLastFilter  = cms.vstring("Control HLT16", "dummy[pass=1,fail=0]")
        process.TnP_Trigger.Expressions.HLT16CutPt16 = cms.vstring("HLT16CutPt16", "Control16ByPathLastFilter == 1", "Control16ByPathLastFilter")
        process.TnP_Trigger.Cuts.PassHLT16CutPt16  = cms.vstring("PassHLT16CutPt16", "HLT16CutPt16", "0.5")
        print 'Num Cut: PassHLT16CutPt16'
    elif num == "TrkMu6NoVtx":
        process.TnP_Trigger.Categories.Control6ByPathLastFilter = cms.vstring("Control HLT6", "dummy[pass=1,fail=0]")
        process.TnP_Trigger.Expressions.HLT6CutPt6 = cms.vstring("HLT6CutPt6", "Control6ByPathLastFilter == 1", "Control6ByPathLastFilter")
        process.TnP_Trigger.Cuts.PassHLT6CutPt6 = cms.vstring("PassHLT6CutPt6", "HLT6CutPt6", "0.5")
        print 'Num Cut: PassHLT6CutPt6'
    elif num == "Mu50":
        process.TnP_Trigger.Categories.Mu50ByPathLastFilter  = cms.vstring("HLT Mu 50", "dummy[pass=1,fail=0]")
        process.TnP_Trigger.Expressions.Mu50CutPt50 = cms.vstring("Mu50CutPt50", "Mu50ByPathLastFilter == 1", "Mu50ByPathLastFilter")
        process.TnP_Trigger.Cuts.PassMu50CutPt50 = cms.vstring("PassMu50CutPt50", "Mu50CutPt50", "0.5")
        print 'Num Cut: PassMu50CutPt50'
                                    
def FillVariables(par):
    '''Declares only the parameters which are necessary, no more'''
    
    '''Always fill pt'''
    process.TnP_Trigger.Variables.pt  = cms.vstring("muon p_{T}", "0.0", "1000.0", "GeV/c")
    print 'muon pt is filled as variable: 0, 1000, GeV/c'
    
    if par == 'eta':
        process.TnP_Trigger.Variables.eta  = cms.vstring("muon #eta", "-2.5", "2.5", "")
        print 'muon eta is filled as variable: -2.5, 2.5'
    if par == 'phi':
        process.TnP_Trigger.Variables.phi  = cms.vstring("muon #phi", "-3.2", "3.2", "")   
        print 'muon phi is filled as variable: -3.2, 3.2'
    if par == 'pt_eta' or 'newpt_eta':
        process.TnP_Trigger.Variables.abseta  = cms.vstring("muon |#eta|", "0", "2.5", "")
    if par == 'pair_deltaR':
        process.TnP_Trigger.Variables.pair_deltaR  = cms.vstring("deltaR", "0", "4", "")

def FillBin(par,den):
    '''Sets the values of the bin paramters and the bool selections on the denominators'''
    #Parameter 
    if par == 'eta':
        DEN.eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4)
        print 'Set bins: eta'
    elif par == 'phi':
        DEN.phi = cms.vdouble(-3.15, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.15)
        print 'Set bins: phi'
    elif par == 'pair_deltaR':
        DEN.pair_deltaR = cms.vdouble(0., 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 5.0)
    elif par == 'pt_eta':
        DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 120, 1000)
        DEN.abseta = cms.vdouble(0., 0.9, 1.2, 2.1, 2.4)
 
    #Selections
    if den == "pT16" and par == "eta": 
        DEN.pt = cms.vdouble(17, 10000)
        print 'Set probe pt range: 17 - 10000 GeV'
    if den == "pT16" and par == "phi": 
        DEN.pt = cms.vdouble(17, 10000)
        print 'Set probe pt range: 17 - 10000 GeV'
    if den == "pT16" and par == "pt": 
        DEN.pt = cms.vdouble(17, 20, 25, 30, 35, 40, 50, 100, 10000)
        print 'Set probe pt bins: 17, ..., 10000 GeV'
        
    if den == "pT6" and par == "eta": 
        DEN.pt = cms.vdouble(8, 10000)
        print 'Set probe pt range: 8 - 10000 GeV'
    if den == "pT6" and par == "phi": 
        DEN.pt = cms.vdouble(8, 10000)
        print 'Set probe pt range: 8 - 10000 GeV'
    if den == "pT6" and par == "pt": 
        DEN.pt = cms.vdouble(8, 12, 16, 20, 25, 30, 35, 40, 50, 100, 10000)
        print 'Set probe pt bins: 8, ..., 10000 GeV'
        
    if den == "pT50" and par == "eta": 
        DEN.pt = cms.vdouble(50, 1000)
        print 'Set probe pt range: 50 - 1000 GeV'
    if den == "pT50" and par == "phi": 
        DEN.pt = cms.vdouble(50, 1000)
        print 'Set probe pt range: 50 - 1000 GeV'
    if den == "pT50" and par == "pt": 
        DEN.pt = cms.vdouble(50, 60, 70, 80, 90, 100, 1000)
        print 'Set probe pt bins: 50, ..., 1000 GeV'

args = sys.argv[1:]

if len(args) > 1: num = args[1]
print 'The num is ', num 

if len(args) > 2: den = args[2]
print 'The den is ', den 

if len(args) > 3: scenario = args[3]
print "Will run scenario ", scenario

if len(args) > 4: sample = args[4]
print 'The sample is ', sample

if len(args) > 5: par = args[5]
print 'The binning is ', par 

bgFitFunction = 'default'
if len(args) > 6: bgFitFunction = args[6]
if bgFitFunction == 'custom':
    print 'Will experiment with custom fit functions'
else:
    print 'Will use the deault fit functions for the backgroud'

print '--------------------'

process = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

if not num  in ['TrkMu16NoVtx', 'TrkMu6NoVtx', 'Mu50']:
    print '@ERROR: num should be in ',['TrkMu16NoVtx', 'TrkMu6NoVtx', 'Mu50'], 'You used', num, '.Abort'
    sys.exit()
if not den in ['pT16', 'pT6', 'pT50']:
    print '@ERROR: den should be',['pT16', 'pT6', 'pT50'], 'You used', den, '.Abort'
    sys.exit()
if not par in  ['pt', 'eta', 'phi', 'pt_eta', 'pair_deltaR']:
    print '@ERROR: par should be', ['pt', 'eta', 'phi', 'pt_eta', 'pair_deltaR'], 'You used', par, '.Abort'

#_*_*_*_*_*_*_*_*_*_*_*_*
#Prepare variables, den, num and fit funct
#_*_*_*_*_*_*_*_*_*_*_*_*

#Set-up the mass range
_mrange = "75"
print 'Lower mass range is', _mrange

Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(True),
    Variables = cms.PSet(),
    Categories = cms.PSet(),
    Expressions = cms.PSet(),
    Cuts = cms.PSet(),
    PDFs = cms.PSet(
        voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[91,84,98], width[2.495], sigma[3,1,20])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        voigtPlusCMS = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            "RooCMSShape::backgroundPass(mass, alphaPass[120.,105.,130.], betaPass[0.02, 0.01,0.1], gammaPass[0.001, 0.,0.1], peakPass[91.5])",
            "RooCMSShape::backgroundFail(mass, alphaFail[120.,105.,130.], betaFail[0.02, 0.01,0.1], gammaFail[0.001, 0.,0.1], peakPass[91.5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
    ),
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    saveDistributionsPlot = cms.bool(False),
    Efficiencies = cms.PSet(), # will be filled later
)

if sample == "2018":
    process.TnP_Trigger = Template.clone(                                                                                                 
        InputFileNames = cms.vstring(                            
            '/afs/cern.ch/work/w/wshi/public/2018DataControlHLT/CMSSW_10_2_0/src/MuonAnalysis/TagAndProbe/test/zmumu/tnpZ_Data_All_Skim_Control_16.root'
            ),     
        InputDirectoryName = cms.string("tpTree"), 
        InputTreeName = cms.string("fitter_tree"),                                                                                     
        OutputFileName = cms.string("TnP_Trigger_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
    )

Sel_dic = {'TrkMu16NoVtx':'PassHLT16CutPt16', 'TrkMu6NoVtx':'PassHLT6CutPt6', 'Mu50':"PassMu50CutPt50"}

FillVariables(par)
FillNumDen(num)

print 'Dic: ', par,' : ',Sel_dic[num]

#_*_*_*_*_*_*_*_*_*_*_*
#Launch fit production
#_*_*_*_*_*_*_*_*_*_*_*
    
#DEFAULT FIT FUNCTION
shape = cms.vstring("voigtPlusExpo")
print 'Default fit func: voigtPlusExpo'

DEN = cms.PSet();
FillBin(par,den)
    
if bgFitFunction == 'default':          
    if ('pt' in par):
        shape = cms.vstring("voigtPlusExpo")
        print 'Fit func updated: voigtPlusExpo'
        #special fit function for one bin in MC (most populated bin)
        if scenario == 'mc_all':
            #C16 trigger
            if (len(DEN.pt)==9):
                shape = cms.vstring("voigtPlusExpo","*pt_bin5*","voigtPlusCMS")
            #C6 trigger
            if (len(DEN.pt)==11):
                shape = cms.vstring("voigtPlusExpo","*pt_bin7*","voigtPlusCMS")
                    
mass_variable ="mass"

#compute efficiency, same for mc and data
print 'Fitting'
setattr(process.TnP_Trigger.Efficiencies, "Wei", cms.PSet(
    EfficiencyCategoryAndState = cms.vstring(Sel_dic[num],"above"),
    UnbinnedVariables = cms.vstring(mass_variable),
    BinnedVariables = DEN,
    BinToPDFmap = shape
    )
       )
            
process.p = cms.Path(
    process.TnP_Trigger
)
