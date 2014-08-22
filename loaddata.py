#!flask/bin/python
from app import db, models
from datetime import datetime

e = models.Event(name='The Grand Final',start=datetime.strptime("28/09/14 14:30", "%d/%m/%y %H:%M"))
db.session.add(e)

m1 = models.Market(name='Half Time Margin',event=e)
m2 = models.Market(name='Full Time Margin',event=e)
m3 = models.Market(name='First Goal 1st Qtr',event=e)
m4 = models.Market(name='First Goal 2nd Qtr',event=e)
m5 = models.Market(name='First Goal 3rd Qtr',event=e)
m6 = models.Market(name='First Goal 4th Qtr',event=e)
m7 = models.Market(name='First Score Combo',event=e)
m8 = models.Market(name='Most Goals by Player'event=e)
m9 = models.Market(name='Qtr By Qtr Lead',event=e)
m10 = models.Market(name='Total Goals',event=e)
m11 = models.Market(name='Total Score',event=e)
db.session.add(m1)
db.session.add(m2)
db.session.add(m3)
db.session.add(m4)
db.session.add(m5)
db.session.add(m6)
db.session.add(m7)
db.session.add(m8)
db.session.add(m9)
db.session.add(m10)
db.session.add(m11)

# Half Time Margin
db.session.add(models.Selection(name='Hawthorn 1-6',market=m1))
db.session.add(models.Selection(name='Hawthorn 7-12',market=m1))
db.session.add(models.Selection(name='Hawthorn 13-18',market=m1))
db.session.add(models.Selection(name='Hawthorn 19-24',market=m1))
db.session.add(models.Selection(name='Hawthorn 25-30',market=m1))
db.session.add(models.Selection(name='Hawthorn 31-36',market=m1))
db.session.add(models.Selection(name='Hawthorn 37-42',market=m1))
db.session.add(models.Selection(name='Hawthorn 43+',market=m1))
db.session.add(models.Selection(name='Fremantle 1-6',market=m1))
db.session.add(models.Selection(name='Fremantle 7-12',market=m1))
db.session.add(models.Selection(name='Fremantle 13-18',market=m1))
db.session.add(models.Selection(name='Fremantle 19-24',market=m1))
db.session.add(models.Selection(name='Fremantle 25-30',market=m1))
db.session.add(models.Selection(name='Fremantle 31-36',market=m1))
db.session.add(models.Selection(name='Fremantle 37-42',market=m1))
db.session.add(models.Selection(name='Fremantle 43+',market=m1))

# Full Time Margin
db.session.add(models.Selection(name='Hawthorn 1-12',market=m2))
db.session.add(models.Selection(name='Hawthorn 13-24',market=m2))
db.session.add(models.Selection(name='Hawthorn 25-36',market=m2))
db.session.add(models.Selection(name='Hawthorn 37-48',market=m2))
db.session.add(models.Selection(name='Hawthorn 49-60',market=m2))
db.session.add(models.Selection(name='Hawthorn 61-72',market=m2))
db.session.add(models.Selection(name='Hawthorn 73-84',market=m2))
db.session.add(models.Selection(name='Hawthorn 85+',market=m2))
db.session.add(models.Selection(name='Fremantle 1-12',market=m2))
db.session.add(models.Selection(name='Fremantle 13-24',market=m2))
db.session.add(models.Selection(name='Fremantle 25-36',market=m2))
db.session.add(models.Selection(name='Fremantle 37-48',market=m2))
db.session.add(models.Selection(name='Fremantle 49-60',market=m2))
db.session.add(models.Selection(name='Fremantle 61-72',market=m2))
db.session.add(models.Selection(name='Fremantle 73-84',market=m2))
db.session.add(models.Selection(name='Fremantle 85+',market=m2))

# First Goal 1st Qtr
db.session.add(models.Selection(name='Hale, David (Hawthorn #20)',market=m3))
db.session.add(models.Selection(name='Pavlich, Matthew (Fremantle #29)',market=m3))
db.session.add(models.Selection(name='Franklin, Lance (Hawthorn #23)',market=m3))
db.session.add(models.Selection(name='Roughead, Jarryd (Hawthorn #2)',market=m3))
db.session.add(models.Selection(name='Any other player',market=m3))
db.session.add(models.Selection(name='Gunston, Jack (Hawthorn #19)',market=m3))
db.session.add(models.Selection(name='Breust, Luke (Hawthorn #22)',market=m3))
db.session.add(models.Selection(name='Crowley, Ryan (Fremantle #15)',market=m3))
db.session.add(models.Selection(name='Lewis, Jordan (Hawthorn #3)',market=m3))
db.session.add(models.Selection(name='Walters, Michael (Fremantle #10)',market=m3))
db.session.add(models.Selection(name='Bailey, Max (Hawthorn #39)',market=m3))
db.session.add(models.Selection(name='Mzungu, Tendai (Fremantle #13)',market=m3))
db.session.add(models.Selection(name='Hill, Stephen (Fremantle #32)',market=m3))
db.session.add(models.Selection(name='Puopolo, Paul (Hawthorn #28)',market=m3))
db.session.add(models.Selection(name='Sandilands, Aaron (Fremantle #31)',market=m3))
db.session.add(models.Selection(name='Sewell, Brad (Hawthorn #12)',market=m3))
db.session.add(models.Selection(name='Barlow, Michael (Fremantle #21)',market=m3))
db.session.add(models.Selection(name='Hill, Brad (Hawthorn #10)',market=m3))
db.session.add(models.Selection(name='Rioli, Cyril (Hawthorn #33)',market=m3))
db.session.add(models.Selection(name='Sutcliffe, Cameron (Fremantle #33)',market=m3))
db.session.add(models.Selection(name='Ballantyne, Hayden (Fremantle #1)',market=m3))
db.session.add(models.Selection(name='Mitchell, Sam (Hawthorn #5)',market=m3))
db.session.add(models.Selection(name='Mundy, David (Fremantle #16)',market=m3))
db.session.add(models.Selection(name='Smith, Isaac (Hawthorn #16)',market=m3))
db.session.add(models.Selection(name='de Boer, Matt (Fremantle #9)',market=m3))
db.session.add(models.Selection(name='Clarke, Zac (Fremantle #30)',market=m3))
db.session.add(models.Selection(name='Mayne, Chris (Fremantle #23)',market=m3))

# First Goal 2nd Qtr
db.session.add(models.Selection(name='Hale, David (Hawthorn #20)',market=m4))
db.session.add(models.Selection(name='Pavlich, Matthew (Fremantle #29)',market=m4))
db.session.add(models.Selection(name='Franklin, Lance (Hawthorn #23)',market=m4))
db.session.add(models.Selection(name='Roughead, Jarryd (Hawthorn #2)',market=m4))
db.session.add(models.Selection(name='Any other player',market=m4))
db.session.add(models.Selection(name='Gunston, Jack (Hawthorn #19)',market=m4))
db.session.add(models.Selection(name='Breust, Luke (Hawthorn #22)',market=m4))
db.session.add(models.Selection(name='Crowley, Ryan (Fremantle #15)',market=m4))
db.session.add(models.Selection(name='Lewis, Jordan (Hawthorn #3)',market=m4))
db.session.add(models.Selection(name='Walters, Michael (Fremantle #10)',market=m4))
db.session.add(models.Selection(name='Bailey, Max (Hawthorn #39)',market=m4))
db.session.add(models.Selection(name='Mzungu, Tendai (Fremantle #13)',market=m4))
db.session.add(models.Selection(name='Hill, Stephen (Fremantle #32)',market=m4))
db.session.add(models.Selection(name='Puopolo, Paul (Hawthorn #28)',market=m4))
db.session.add(models.Selection(name='Sandilands, Aaron (Fremantle #31)',market=m4))
db.session.add(models.Selection(name='Sewell, Brad (Hawthorn #12)',market=m4))
db.session.add(models.Selection(name='Barlow, Michael (Fremantle #21)',market=m4))
db.session.add(models.Selection(name='Hill, Brad (Hawthorn #10)',market=m4))
db.session.add(models.Selection(name='Rioli, Cyril (Hawthorn #33)',market=m4))
db.session.add(models.Selection(name='Sutcliffe, Cameron (Fremantle #33)',market=m4))
db.session.add(models.Selection(name='Ballantyne, Hayden (Fremantle #1)',market=m4))
db.session.add(models.Selection(name='Mitchell, Sam (Hawthorn #5)',market=m4))
db.session.add(models.Selection(name='Mundy, David (Fremantle #16)',market=m4))
db.session.add(models.Selection(name='Smith, Isaac (Hawthorn #16)',market=m4))
db.session.add(models.Selection(name='de Boer, Matt (Fremantle #9)',market=m4))
db.session.add(models.Selection(name='Clarke, Zac (Fremantle #30)',market=m4))
db.session.add(models.Selection(name='Mayne, Chris (Fremantle #23)',market=m4))

# First Goal 3rd Qtr
db.session.add(models.Selection(name='Hale, David (Hawthorn #20)',market=m5))
db.session.add(models.Selection(name='Pavlich, Matthew (Fremantle #29)',market=m5))
db.session.add(models.Selection(name='Franklin, Lance (Hawthorn #23)',market=m5))
db.session.add(models.Selection(name='Roughead, Jarryd (Hawthorn #2)',market=m5))
db.session.add(models.Selection(name='Any other player',market=m5))
db.session.add(models.Selection(name='Gunston, Jack (Hawthorn #19)',market=m5))
db.session.add(models.Selection(name='Breust, Luke (Hawthorn #22)',market=m5))
db.session.add(models.Selection(name='Crowley, Ryan (Fremantle #15)',market=m5))
db.session.add(models.Selection(name='Lewis, Jordan (Hawthorn #3)',market=m5))
db.session.add(models.Selection(name='Walters, Michael (Fremantle #10)',market=m5))
db.session.add(models.Selection(name='Bailey, Max (Hawthorn #39)',market=m5))
db.session.add(models.Selection(name='Mzungu, Tendai (Fremantle #13)',market=m5))
db.session.add(models.Selection(name='Hill, Stephen (Fremantle #32)',market=m5))
db.session.add(models.Selection(name='Puopolo, Paul (Hawthorn #28)',market=m5))
db.session.add(models.Selection(name='Sandilands, Aaron (Fremantle #31)',market=m5))
db.session.add(models.Selection(name='Sewell, Brad (Hawthorn #12)',market=m5))
db.session.add(models.Selection(name='Barlow, Michael (Fremantle #21)',market=m5))
db.session.add(models.Selection(name='Hill, Brad (Hawthorn #10)',market=m5))
db.session.add(models.Selection(name='Rioli, Cyril (Hawthorn #33)',market=m5))
db.session.add(models.Selection(name='Sutcliffe, Cameron (Fremantle #33)',market=m5))
db.session.add(models.Selection(name='Ballantyne, Hayden (Fremantle #1)',market=m5))
db.session.add(models.Selection(name='Mitchell, Sam (Hawthorn #5)',market=m5))
db.session.add(models.Selection(name='Mundy, David (Fremantle #16)',market=m5))
db.session.add(models.Selection(name='Smith, Isaac (Hawthorn #16)',market=m5))
db.session.add(models.Selection(name='de Boer, Matt (Fremantle #9)',market=m5))
db.session.add(models.Selection(name='Clarke, Zac (Fremantle #30)',market=m5))
db.session.add(models.Selection(name='Mayne, Chris (Fremantle #23)',market=m5))

# First Goal 4th Qtr
db.session.add(models.Selection(name='Hale, David (Hawthorn #20)',market=m6))
db.session.add(models.Selection(name='Pavlich, Matthew (Fremantle #29)',market=m6))
db.session.add(models.Selection(name='Franklin, Lance (Hawthorn #23)',market=m6))
db.session.add(models.Selection(name='Roughead, Jarryd (Hawthorn #2)',market=m6))
db.session.add(models.Selection(name='Any other player',market=m6))
db.session.add(models.Selection(name='Gunston, Jack (Hawthorn #19)',market=m6))
db.session.add(models.Selection(name='Breust, Luke (Hawthorn #22)',market=m6))
db.session.add(models.Selection(name='Crowley, Ryan (Fremantle #15)',market=m6))
db.session.add(models.Selection(name='Lewis, Jordan (Hawthorn #3)',market=m6))
db.session.add(models.Selection(name='Walters, Michael (Fremantle #10)',market=m6))
db.session.add(models.Selection(name='Bailey, Max (Hawthorn #39)',market=m6))
db.session.add(models.Selection(name='Mzungu, Tendai (Fremantle #13)',market=m6))
db.session.add(models.Selection(name='Hill, Stephen (Fremantle #32)',market=m6))
db.session.add(models.Selection(name='Puopolo, Paul (Hawthorn #28)',market=m6))
db.session.add(models.Selection(name='Sandilands, Aaron (Fremantle #31)',market=m6))
db.session.add(models.Selection(name='Sewell, Brad (Hawthorn #12)',market=m6))
db.session.add(models.Selection(name='Barlow, Michael (Fremantle #21)',market=m6))
db.session.add(models.Selection(name='Hill, Brad (Hawthorn #10)',market=m6))
db.session.add(models.Selection(name='Rioli, Cyril (Hawthorn #33)',market=m6))
db.session.add(models.Selection(name='Sutcliffe, Cameron (Fremantle #33)',market=m6))
db.session.add(models.Selection(name='Ballantyne, Hayden (Fremantle #1)',market=m6))
db.session.add(models.Selection(name='Mitchell, Sam (Hawthorn #5)',market=m6))
db.session.add(models.Selection(name='Mundy, David (Fremantle #16)',market=m6))
db.session.add(models.Selection(name='Smith, Isaac (Hawthorn #16)',market=m6))
db.session.add(models.Selection(name='de Boer, Matt (Fremantle #9)',market=m6))
db.session.add(models.Selection(name='Clarke, Zac (Fremantle #30)',market=m6))
db.session.add(models.Selection(name='Mayne, Chris (Fremantle #23)',market=m6))

# First Score Combo
db.session.add(models.Selection(name='Behind-Goal-Goal-Behind',market=m7))
db.session.add(models.Selection(name='Behind-Behind-Goal-Behind',market=m7))
db.session.add(models.Selection(name='Goal-Behind-Behind-Goal',market=m7))
db.session.add(models.Selection(name='Behind-Behind-Goal-Goal',market=m7))
db.session.add(models.Selection(name='Goal-Behind-Goal-Goal',market=m7))
db.session.add(models.Selection(name='Goal-Behind-Goal-Behind',market=m7))
db.session.add(models.Selection(name='Goal-Behind-Behind-Behind',market=m7))
db.session.add(models.Selection(name='Goal-Goal-Goal-Goal',market=m7))
db.session.add(models.Selection(name='Goal-Goal-Behind-Goal',market=m7))
db.session.add(models.Selection(name='Behind-Goal-Goal-Goal',market=m7))
db.session.add(models.Selection(name='Goal-Goal-Behind-Behind',market=m7))
db.session.add(models.Selection(name='Behind-Behind-Behind-Behind',market=m7))
db.session.add(models.Selection(name='Behind-Behind-Behind-Goal',market=m7))
db.session.add(models.Selection(name='Behind-Goal-Behind-Goal',market=m7))
db.session.add(models.Selection(name='Behind-Goal-Behind-Behind',market=m7))
db.session.add(models.Selection(name='Goal-Goal-Goal-Behind',market=m7))

# Most Goals by Player
db.session.add(models.Selection(name='Hale, David (Hawthorn #20)',market=m8))
db.session.add(models.Selection(name='Roughead, Jarryd (Hawthorn #2)',market=m8))
db.session.add(models.Selection(name='Gunston, Jack (Hawthorn #19)',market=m8))
db.session.add(models.Selection(name='Rioli, Cyril (Hawthorn #33)',market=m8))
db.session.add(models.Selection(name='Franklin, Lance (Hawthorn #23)',market=m8))
db.session.add(models.Selection(name='Any other player',market=m8))
db.session.add(models.Selection(name='Walters, Michael (Fremantle #10)',market=m8))
db.session.add(models.Selection(name='Puopolo, Paul (Hawthorn #28)',market=m8))
db.session.add(models.Selection(name='Pavlich, Matthew (Fremantle #29)',market=m8))
db.session.add(models.Selection(name='Breust, Luke (Hawthorn #22)',market=m8))
db.session.add(models.Selection(name='Hale, David (Hawthorn #20)',market=m8))
db.session.add(models.Selection(name='Walters, Michael (Fremantle #10)',market=m8))
db.session.add(models.Selection(name='Lewis, Jordan (Hawthorn #3)',market=m8))
db.session.add(models.Selection(name='Puopolo, Paul (Hawthorn #28)',market=m8))
db.session.add(models.Selection(name='Breust, Luke (Hawthorn #22)',market=m8))
db.session.add(models.Selection(name='Pavlich, Matthew (Fremantle #29)',market=m8))
db.session.add(models.Selection(name='Mayne, Chris (Fremantle #23)',market=m8))
db.session.add(models.Selection(name='Rioli, Cyril (Hawthorn #33)',market=m8))
db.session.add(models.Selection(name='Franklin, Lance (Hawthorn #23)',market=m8))
db.session.add(models.Selection(name='Mayne, Chris (Fremantle #23)',market=m8))
db.session.add(models.Selection(name='Clarke, Zac (Fremantle #30)',market=m8))
db.session.add(models.Selection(name='Ballantyne, Hayden (Fremantle #1)',market=m8))
db.session.add(models.Selection(name='Roughead, Jarryd (Hawthorn #2)',market=m8))
db.session.add(models.Selection(name='Gunston, Jack (Hawthorn #19)',market=m8))
db.session.add(models.Selection(name='Lewis, Jordan (Hawthorn #3)',market=m8))
db.session.add(models.Selection(name='Clarke, Zac (Fremantle #30)',market=m8))
db.session.add(models.Selection(name='Ballantyne, Hayden (Fremantle #1)',market=m8))

# Qtr By Qtr Lead
Draw at end of any quarter
Fremantle-Fremantle-Fremantle-Fremantle	$9.40	Add Winner
Hawthorn-Fremantle-Fremantle-Hawthorn	$15.67	Add Winner
Hawthorn-Fremantle-Hawthorn-Hawthorn	$23.50	Add Winner
Hawthorn-Hawthorn-Hawthorn-Hawthorn	$23.50	Remove Winner
Fremantle-Fremantle-Hawthorn-Hawthorn	$23.50	Add Winner
Fremantle-Hawthorn-Fremantle-Fremantle	$23.50	Add Winner
Hawthorn-Fremantle-Fremantle-Fremantle	$47.00	Add Winner
Hawthorn-Hawthorn-Fremantle-Fremantle	$47.00	Add Winner
Hawthorn-Fremantle-Hawthorn-Fremantle	$47.00	Add Winner
Hawthorn-Hawthorn-Fremantle-Hawthorn	$47.00	Add Winner
Fremantle-Fremantle-Fremantle-Hawthorn	$47.00	Add Winner
Hawthorn-Hawthorn-Hawthorn-Fremantle	$47.00	Add Winner
Fremantle-Hawthorn-Hawthorn-Fremantle	$47.00	Add Winner
Fremantle-Hawthorn-Fremantle-Hawthorn	$47.00	Add Winner
Fremantle-Fremantle-Hawthorn-Fremantle	$47.00	Add Winner
Fremantle-Hawthorn-Hawthorn-Hawthorn




m10 = models.Market(name='Total Goals',event=e)
m11 = models.Market(name='Total Score',event=e)










db.session.commit()
