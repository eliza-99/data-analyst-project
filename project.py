import pandas as pd
gameplay=pd.read_csv("gameplay.csv")
gameplay=gameplay.rename(columns={'User ID':'user_id','Games Played':'games_played'})
gameplay['Datetime'] = pd.to_datetime(gameplay['Datetime'], format='%d-%m-%Y %H:%M')
gameplay['date']=gameplay['Datetime'].dt.date
gameplay['hour']=gameplay['Datetime'].dt.hour
gameplay['slot']=gameplay['hour'].apply(lambda x:'slot1' if x<12 else 'slot2')
gameplay=gameplay.groupby(['user_id','date','slot'])['games_played'].sum().reset_index(name='total_games')
print (gameplay)
deposite=pd.read_csv("deposite.csv")
deposite=deposite.rename(columns={'User Id':'user_id','Amount':'deposite_amount'})
deposite['Datetime'] = pd.to_datetime(deposite['Datetime'], format='%d-%m-%Y %H:%M')
deposite['date']=deposite['Datetime'].dt.date
deposite['hour']=deposite['Datetime'].dt.hour
deposite['slot']=deposite['hour'].apply(lambda x:'slot1' if x<12 else 'slot2')
# Group by user_id, date, and slot
deposit_summary = deposite.groupby(['user_id', 'date', 'slot']).agg(
    total_deposit=('deposite_amount', 'sum'),
    deposit_count=('deposite_amount', 'count')
).reset_index()

print(deposit_summary)
#print(deposite)
withdrawl=pd.read_csv("withdrawl.csv")
withdrawl=withdrawl.rename(columns={'User Id':'user_id','Amount':'withdrawl_amount'})
withdrawl['Datetime'] = pd.to_datetime(deposite['Datetime'], format='%d-%m-%Y %H:%M')
withdrawl['date']=withdrawl['Datetime'].dt.date
withdrawl['hour']=withdrawl['Datetime'].dt.hour
withdrawl['slot']=withdrawl['hour'].apply(lambda x:'slot1' if x<12 else 'slot2')
# Group by user_id, date, and slot
withdrawl_summary = withdrawl.groupby(['user_id', 'date', 'slot']).agg(
    total_withdrawl=('withdrawl_amount', 'sum'),
    withdrawl_count=('withdrawl_amount', 'count')
).reset_index()
print(withdrawl_summary)
#print(withdrawl)
table=pd.merge(gameplay,deposit_summary, on=['user_id','date','slot'],how='outer')
print (table)
game_details=pd.merge(table,withdrawl_summary,on=['user_id','date','slot'],how='outer')
game_details.fillna(0,inplace=True)
print (game_details)
# Fill NaN with 0 first (to avoid errors)
#game_details = game_details.fillna(0)

# Convert all numeric columns to int (excluding user_id/date/slot)
for col in game_details.columns:
    if col not in ['user_id', 'date', 'slot','total_deposit','total_withdrawl']:
        game_details[col] = game_details[col].astype(int)
print(game_details)
game_details.to_csv("game_summary.csv",index=False)
