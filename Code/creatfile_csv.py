from pandas import *
zone,pm25,date,time,station,website = [],[],[],[],[],[]
zone = ['ต.นาจักร อ.เมือง จ.แพร่',
        'ต.สบป้าด อ.แม่เมาะ จ.ลำปาง',
        'ต.บ้านต๋อม อ.เมือง จ.พะเยา',
        'ต.ในเวียง อ.เมือง จ.น่าน',
        'ต.เวียงพางคำ อ.แม่สาย จ.เชียงราย',
        'ต.จองคำ อ.เมือง จ.แม่ฮ่องสอน',
        'ต.บ้านกลาง อ.เมือง จ.ลำพูน',
        'ต.ศรีภูมิ อ.เมือง จ.เชียงใหม่',
        'ต.แม่ปะ อ.แม่สอด จ.ตาก',
        'ต.คลองหนึ่ง อ.คลองหลวง จ.ปทุมธานี']

pm25 = [259,180,112,99,56,36,54,63,79,33]
date = ['1/28/2020',
        '1/28/2020',
        '1/28/2020',
        '1/28/2020',
        '1/28/2020',
        '1/28/2020',
        '1/28/2020',
        '1/28/2020',
        '1/28/2020',
        '1/28/2020',]

time = ['11:00 - 12:00',
        '11:00 - 12:00',
        '11:00 - 12:00',
        '11:00 - 12:00',
        '11:00 - 12:00',
        '11:00 - 12:00',
        '11:00 - 12:00',
        '11:00 - 12:00',
        '11:00 - 12:00',
        '11:00 - 12:00',]

station = ['69t อุตุนิยมวิทยาจังหวัดแพร่ undefined',
           '38t โรงพยาบาลส่งเสริมสุขภาพตำบลบ้านสบป้าด undefined',
           '70t อุทยานการเรียนรู้ องค์การบริหารส่วนจังหวัดพะเยา undefined',
           '67t สำนักงานเทศบาลเมืองน่าน undefined',
           '73t สำนักงานสาธารณสุขแม่สาย undefined',
           '58t สำนักงานทรัพยากรธรรมชาติและสิ่งแวดล้อมจังหวัดแม่ฮ่องสอน undefined',
           '68t สถานีอุตุนิยมวิทยาจังหวัดลำพูน undefined',
           '36t โรงเรียนยุพราชวิทยาลัย undefined',
           '76t ศูนย์การศึกษานอกโรงเรียน undefined',
           '20t มหาวิทยาลัยกรุงเทพ วิทยาเขตรังสิต undefined',]

website = ['http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',
           'http://air4thai.pcd.go.th/webV2/history/',]

result = {'ZONE': zone,
          'PM2.5': pm25,
          'DATE': date,
          'TIME': time,
          'STATION': station,
          'WEBSITE': website}
outfile = DataFrame(result)
outfile.to_csv('files/pm25.csv',index=0)