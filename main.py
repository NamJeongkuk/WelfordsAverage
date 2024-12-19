varList = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
varList2 = [47, 50, 54, 50, 49, 57, 55, 49, 49, 56, 41, 46, 48, 49, 51, 52, 49, 45, 50, 50, 38, 48, 37, 46, 57, 53, 48, 53, 48, 54, 48, 51, 48, 53, 48, 55, 47, 56, 44, 51, 54, 53, 61, 58, 53, 43, 50, 53, 48, 57, 48, 44, 59, 52, 52, 52, 47, 52, 46, 55, 46, 45, 50, 46, 57, 47, 50, 44, 50, 45, 55, 49, 55, 46, 45, 48, 52, 50, 51, 44, 47, 40, 54, 50, 50, 56, 44, 49, 44, 48, 39, 55, 53, 45, 55, 58, 51, 52, 53, 43, 43, 40, 46, 49, 48, 47, 48, 55, 40, 52, 49, 50, 40, 55, 46, 38, 54, 49, 50, 46, 47, 48, 50, 47, 52, 57, 50, 47, 64, 50, 44, 52, 45, 52, 45, 53, 53, 45, 55, 44, 39, 48, 51, 48, 55, 49, 56, 44, 54, 49, 56, 50, 54, 57, 54, 44, 46, 48, 53, 42, 45, 47, 44, 52, 47, 57, 46, 49, 54, 52, 44, 51, 38, 47, 55, 49, 43, 52, 46, 40, 49, 55, 51, 52, 54, 45, 41, 45, 51, 45, 46, 51, 48, 55, 47, 54, 53, 61, 46, 48, 52, 54, 52, 56, 52, 45, 47, 53, 42, 57, 53, 55, 47, 51, 63, 40, 51, 47, 59, 51, 53, 45, 58, 51, 53, 53, 48, 44, 47, 50, 50, 47, 53, 47, 54, 49, 44, 58, 50, 48, 39, 50, 57, 55, 46, 57, 46, 46, 55, 45, 48, 48, 48, 45, 41, 44, 48, 49, 51, 44, 50, 46, 58, 41, 50, 54, 47, 56, 43, 46, 47, 52, 49, 31, 47, 51, 52, 52, 44, 57, 46, 48, 50, 53, 49, 64, 49, 62, 43, 50, 62, 47, 45, 46, 49, 53, 45, 55, 54, 60, 42, 48, 50, 51, 46, 51, 55, 47, 41, 42, 52, 53, 54, 54, 55, 51, 45, 53, 48, 43, 48, 60, 49, 51, 43, 47, 59, 47, 43, 48, 43, 46, 54, 51, 46, 43, 46, 55, 45, 47, 53, 46, 61, 52, 54, 42, 45, 55, 43, 47, 43, 52, 41, 51, 46, 47, 37, 57, 40, 54, 52, 58, 49, 46, 61, 54, 51, 49, 57, 49, 45, 50, 47, 50, 51, 56, 59, 61, 53, 45, 51, 48, 45, 39, 42, 46, 55, 54, 48, 41, 51, 57, 55, 44, 59, 43, 49, 46, 56, 49, 50, 53, 36, 44, 46, 46, 42, 41, 41, 48, 52, 58, 51, 53, 55, 48, 48, 51, 49, 48, 47, 58, 46, 49, 52, 57, 45, 44, 52, 55, 45, 54, 51, 47, 46, 45, 54, 40, 57, 44, 38, 50, 44, 51, 47, 39, 47, 50, 50, 42, 61, 44, 55, 53, 58, 51, 50, 52, 49, 44, 43, 41, 47, 54, 44, 56, 49, 53, 48, 43, 53, 50, 47, 53, 40, 42, 48, 38, 49, 50, 50, 52, 50, 40, 51, 46, 49, 49, 50, 43, 49, 46, 53, 40, 47, 50, 47, 57, 50, 54, 42, 56, 58, 43, 55, 49, 48, 47, 46, 56, 43, 51, 49, 37, 49, 47, 51, 54, 40, 55, 49, 44, 48, 48, 57, 52, 61, 43, 52, 54, 43, 49, 62, 51, 56, 52, 48, 52, 49, 54, 61, 53, 53, 51, 43, 55, 52, 50, 49, 48, 44, 43, 52, 45, 51, 55, 49, 49, 50, 55, 51, 41, 57, 50, 47, 53, 55, 52, 47, 48, 51, 49, 50, 45, 52, 52, 47, 49, 51, 52, 42, 43, 46, 49, 49, 36, 41, 51, 66, 45, 51, 48, 40, 49, 51, 47, 50, 41, 45, 48, 50, 49, 49, 47, 51, 55, 49, 53, 45, 48, 50, 45, 53, 61, 52, 48, 44, 47, 48, 56, 49, 58, 45, 57, 52, 55, 49, 54, 53, 46, 53, 49, 51, 57, 51, 53, 39, 51, 49, 54, 55, 49, 46, 48, 51, 51, 52, 47, 47, 42, 51, 36, 44, 48, 52, 50, 49, 45, 54, 41, 49, 52, 48, 47, 40, 45, 47, 50, 48, 41, 54, 44, 54, 50, 40, 45, 53, 42, 52, 46, 47, 49, 52, 53, 41, 55, 49, 56, 50, 49, 43, 51, 49, 47, 53, 51, 57, 50, 51, 49, 50, 57, 50, 53, 41, 51, 45, 49, 52, 50, 51, 47, 66, 50, 47, 56, 48, 41, 54, 48, 45, 43, 45, 49, 45, 60, 44, 48, 46, 46, 43, 45, 53, 51, 40, 49, 56, 50, 63, 48, 51, 45, 41, 50, 46, 46, 50, 57, 41, 35]

def meanFunction(PREV_MEAN, NUM_OF_SAMPLE, NEW_SAMPLE_VALUE):

  PREV_TOTAL_VALUE = PREV_MEAN * (NUM_OF_SAMPLE - 1) # prevent overflow here!
  NEW_TOTAL = PREV_TOTAL_VALUE + NEW_SAMPLE_VALUE

  return NEW_TOTAL/NUM_OF_SAMPLE

def welfordFunction(PREV_MEAN, NUM_OF_SAMPLE, NEW_SAMPLE_VALUE):
  
  return (PREV_MEAN) + (NEW_SAMPLE_VALUE - PREV_MEAN) / NUM_OF_SAMPLE

def welfordFunctionWithMaxBound(PREV_MEAN, NUM_OF_SAMPLE, NEW_SAMPLE_VALUE, MAX):
  
  if NUM_OF_SAMPLE > MAX : NUM_OF_SAMPLE = MAX

  return (PREV_MEAN) + (NEW_SAMPLE_VALUE - PREV_MEAN) / NUM_OF_SAMPLE


PrevMean = 0
welfordPrevMean = 0
welfordPrevMeanMaxed = 0

SELECTED_LIST = varList2

for LOOP0 in range(0,len(SELECTED_LIST) - 1):
  
  
  NTH_CALC = LOOP0 + 1
  NEW_VALUE = SELECTED_LIST[LOOP0]

  PrevMean =  meanFunction(PrevMean, NTH_CALC, NEW_VALUE)
  welfordPrevMean = welfordFunction(welfordPrevMean, NTH_CALC, NEW_VALUE)
  welfordPrevMeanMaxed = welfordFunctionWithMaxBound(welfordPrevMeanMaxed, NTH_CALC, NEW_VALUE, 600)


  res = "OK" if round(PrevMean, 2) == round(welfordPrevMean, 2) else "Fail"

  print("Mean = {:>10.2f}, Welford Mean = {:<10.2f}, WP Maxed Mean = {:>10.2f}  {}".format(PrevMean, welfordPrevMean, welfordPrevMeanMaxed, res))
