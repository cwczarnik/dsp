# I can't think of another way to do this, so here it is:
df = pd.read_csv('faculty.csv')
df.columns =[u'name', u'degree', u'title', u'email'] 
#print(df.head())
df['email'].to_csv('email.csv')
