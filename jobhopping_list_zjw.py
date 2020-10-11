import pandas as pd

rough_data = pd.read_excel(r'E:\python宇宙\python_examples\zjw_linkedin\20201011_test\rough_droplist.xlsx')
ogn_data = pd.read_excel(r'E:\python宇宙\python_examples\zjw_linkedin\20201011_test\drop_duplicate.xlsx')
id_ls = list(ogn_data["id"])
nm_ls = list(ogn_data["name"])
ix_ls = list(rough_data['index'])
# print(id_ls,nm_ls,ix_ls)
obj = pd.Series(nm_ls, index=id_ls)
#print(obj)
obj2 = obj.reindex(ix_ls)
#print(obj2)
dic={"name":obj2.values}
df = pd.DataFrame(dic)
df.to_excel(r'E:\python宇宙\python_examples\zjw_linkedin\20201011_test\rough_droplist.xlsx',index=False)