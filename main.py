import configcatclient

configcat_client = configcatclient.create_client(
    'OZ7ZCG9ReEeGk8fTobyUCw/aTK_BTzDNUC-BF6_a0rOCQ')

featureone = configcat_client.get_value('featureone', False)
#print('featureone\'s value from ConfigCat: ' + str(featureone))
def kmtomiles():
    #input
    kilometers = float(input("Enter value in kilometers: "))
    conv_fac = 0.621371
    miles = kilometers * conv_fac
    print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
def milestokm():
    miles = float(input("Enter value in miles: "))
    conv_fac = 1.60934
    kilometers = miles * conv_fac
    print('%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))
if featureone:
    kmtomiles()

else:
    milestokm()

