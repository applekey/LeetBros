import * from serviceInclude

#inserts all pertinant dash info per user
def InsertDashInfo(clientId, data):
  ## bills due
  oub = GetOutStandingBills()
  upb = GetUpCommingBills()


  pass


def GetOutStandingBills(config):
  ## read into a tmp table

  billAdap = billAdapter(*dbManager.getDBConfig())
  billAdap.connect()

  pastDueBills = billAdapter.querryPastDueBills()

  billAdap.disconnect()

  return pastDueBills

def GetUpCommingBills(config):

  billAdap = billAdapter(*dbManager.getDBConfig())
  billAdap.connect()

  upCommingBills = billAdapter.querryUpCommingBills(config)

  billAdap.disconnect()

  return upCommingBills

  ## do we link or do we copy all the info to the another table, more data duplication
  # i think its better to have more data duplication, better parallsim
