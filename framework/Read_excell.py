import xlrd
from framework.logger import Logger


logger=Logger("logger=Util").getlog()

class Util(object):
    @classmethod
    def read_excel(cls,excelPath,sheetName="Sheet1"):
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)
        keys=sheet.row_values(0)
        rowNum=sheet.nrows                      #行
        celNum=sheet.ncols                      #列
        if rowNum<=1:
            logger.error("excel表中数据行数小于1")
        else:
            r=[]
            for i in range(1,rowNum):
                sheet_data={}
                values=sheet.row_values(i)
                for j in range(celNum):
                    sheet_data[keys[j]]=values[j]
                r.append(sheet_data)
        return r

if __name__=="__main__":
    filepath = "data.xlsx"
    sheetName = "Sheet1"
    print(Util().read_excel("D:/xlrd.xlsx","Sheet1"))