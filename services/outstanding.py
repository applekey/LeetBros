from serviceInclude import *
from outstanding import *
from dbManager import *
from userAdapter import *
from billAdapter import *

#inserts all pertinant dash info per user
def GetDashInfo(clientId, data):
  ## bills due
  oub = GetOutStandingBills('args')
  upb = GetUpCommingBills('args')
  ## For now just add this to temp table
  ## Need to in the future need to figure out some caching

  return (oub,upb)


def GetOutStandingBills(config):
  ## read into a tmp table

  billAdap = billAdapter(*dbManager.getDBConfig())
  billAdap.connect()

  pastDueBills = billAdap.querryPastDueBills()

  billAdap.disconnect()

  return pastDueBills

def GetUpCommingBills(config):

  billAdap = billAdapter(*dbManager.getDBConfig())
  billAdap.connect()

  upCommingBills = billAdap.querryUpCommingBills()

  billAdap.disconnect()

  return upCommingBills

  ## do we link or do we copy all the info to the another table, more data duplication
  # i think its better to have more data duplication, better parallsim
