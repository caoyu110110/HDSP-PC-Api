import pytest
import os
import allure
from api.baseapi import BaseApi
from api.basic import Basic
from api.admin_web import Adminweb


@allure.feature('test_otainfo_list')
class TestBasic:
    data = BaseApi.yaml_load('../yaml_data/test_basic.yaml')

    def setup(self):
        self.adminweb = Adminweb()
        self.basic = Basic()

    # @pytest.mark.parametrize('data', data['test_otainfo_list_unitName'])
    def test_otainfo_list(self):
        """
        网约房平台信息列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.otainfo_list(token=token)
        assert r['message'] == 'SUCCESS'

    def test_otainfo_detail(self):
        """
        网约房平台详细信息
        :param data:
        :return:
        """
        token = self.adminweb.get_token()
        otaCode = self.basic.otainfo_list(token=token)['data']['hdspOtaInfos'][0]['otaCode']
        # print(otaCode)
        detail = self.basic.otainfo_detail(token=token, otaCode=otaCode)
        assert detail['message'] == 'SUCCESS'

    def test_otainfo_export(self):
        """
        网约房平台导出

        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.otainfo_export(token=token)
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    def test_employee_employeeList(self):
        """
        从业人员管理列表

        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.employee_employeeList(token=token)
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    def test_employee_personInfo(self):
        """
        从业人员管理详情
        :param data:
        :return:
        """
        token = self.adminweb.get_token()
        cardNum = self.basic.employee_employeeList(token=token)['data'][0]['cardNum']
        print("cardNum的值：" + cardNum)
        personInfo = self.basic.employee_personInfo(token=token, cardNum=cardNum)
        assert personInfo['message'] == 'SUCCESS'

    def test_employee_employeeHotelInfo(self):
        """
        从业人员详情-门店
        :param data:
        :return:
        """
        token = self.adminweb.get_token()
        cardNum = self.basic.employee_employeeList(token=token)['data'][0]['cardNum']
        personInfo = self.basic.employee_employeeHotelInfo(token=token, cardNum=cardNum)
        assert personInfo['message'] == 'SUCCESS'

    def test_employee_employeeRoomInfoo(self):
        """
        从业人员详情-房屋
        :param data:
        :return:
        """
        token = self.adminweb.get_token()
        cardNum = self.basic.employee_employeeList(token=token)['data'][0]['cardNum']
        personInfo = self.basic.employee_employeeRoomInfo(token=token, cardNum=cardNum)
        assert personInfo['message'] == 'SUCCESS'

    def test_employee_exportExcel(self):
        """
        导出--从业人员信息列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.otainfo_export(token=token)
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    def test_room_list_all(self):
        """
        房屋列表查询--all
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_list(token=token)
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    @pytest.mark.parametrize('data', data['test_room_list_hotelName'])
    def test_room_list(self, data):
        """
        房屋列表查询--根据门店名称搜索
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_list(token=token, hotelName=data['hotelName'])
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    def test_room_detail(self):
        """
        房屋详情查询
        :param data:
        :return:
        """
        token = self.adminweb.get_token()
        roomCode = self.basic.room_list(token=token)['data']['list'][0]['roomCode']
        detail = self.basic.room_detail(token=token, roomCode=roomCode)
        assert detail['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_room_update'])
    def test_room_list(self, data):
        """
        房屋编辑
        :param data:
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_update(token=token, roomCode=data['roomCode'], bedNum=data['bedNum'],
                                   roomName=data['roomName'], streetName=data['streetName'],
                                   buildingName=data['buildingName'], psbUnitCode=data['psbUnitCode'],
                                   building=data['building'], roomNo=data['roomNo'], isOpen=data['isOpen'],
                                   imgList=data['imgList'], unit=data['unit'], floor=data['floor'], iidd=data['iidd'],
                                   streetCode=data['streetCode'])

        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    @pytest.mark.parametrize('data', data['test_room_unlock_logs'])
    def test_room_unlock_logs(self, data):
        """
        查询房屋下的开锁记录
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_unlock_logs(token=token, roomCode=data['roomCode'])
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    @pytest.mark.parametrize('data', data['test_room_del'])
    def test_room_del(self, data):
        """
        房屋删除
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_del(token=token, roomCode=data['roomCode'], reason=data['reason'], delType=data['delType'])
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    def test_room_check_list(self):
        """
        查询房屋核检查记录列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_check_list(token=token)
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    @pytest.mark.parametrize('data', data['test_room_check_detail'])
    def test_room_check_detail(self, data):
        """
        查询房屋核检查记录详情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_check_detail(token=token, iidd=data['iidd'])
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    @pytest.mark.parametrize('data', data['test_room_checkstate_reset'])
    def test_room_check_detail(self, data):
        """
        重置房屋核查状态
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_checkstate_reset(token=token, roomCode=data['roomCode'], checkId=data['checkId'],
                                             reason=data['reason'])
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    @pytest.mark.parametrize('data', data['test_room_merge'])
    def test_room_merge(self, data):
        """
        合并房屋
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_merge(token=token, proomCode=data['proomCode'], sroomCodeList=data['sroomCodeList'])
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    @pytest.mark.parametrize('data', data['test_room_split'])
    def test_room_split(self, data):
        """
        拆分房屋
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_split(token=token, proomCode=data['proomCode'], sroomCodeList=data['sroomCodeList'])
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    def test_hotel_list_export(self):
        """
        门店列表信息导出
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.hotel_list_export(token=token)
        assert r['message'] == 'SUCCESS'
        assert r['code'] == 0

    def test_room_list_export(self):
        """
        房屋列表信息导出
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_list_export(token=token)
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_room_childs'])
    def test_room_childs(self, data):
        """
        子房屋列表查询
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_childs(token=token, roomCode=data['roomCode'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_room_uploadimg'])
    def test_room_uploadimg(self, data):
        """
        房屋图片上传
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.room_uploadimg(token=token, iidd=data['iidd'], roomCode=data['roomCode'], files=data['files'])
        print(r)

    @pytest.mark.parametrize('data', data['test_calendar_hotelCalendar'])
    def test_calendar_hotelCalendar(self, data):
        """
        门店旅客入住日历
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.calendar_hotelCalendar(token=token, hotelCode=data['hotelCode'], year=data['year'],
                                              month=data['month'])
        assert r['message'] == 'SUCCESS'

    def test_street_list(self):
        """
        获取街路巷列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.street_list(token=token)
        assert r['message'] == 'SUCCESS'

    def test_hotel_list(self):
        """
        门店列表查询
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.hotel_list(token=token)
        assert r['message'] == 'SUCCESS'

    def test_hotel_detail(self):
        """
        门店详情查询
        :return:
        """
        token = self.adminweb.get_token()
        hotel_code = self.basic.hotel_list(token=token)['data']['list'][0]['hotelCode']
        r = self.basic.hotel_detail(token=token, hotelCode=hotel_code)
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_hotel_merchant_update'])
    def test_hotel_merchant_update(self, data):
        """
        门店信息编辑
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.hotel_merchant_update(token=token, hotelCode=data['hotelCode'],
                                             merchantName=data['merchantName'], merchantCardNum=data['merchantCardNum'],
                                             merchantPhone=data['merchantPhone'], hotelAddress=data['hotelAddress'])
        assert r['code'] == 0

    @pytest.mark.parametrize('data', data['test_hotel_rooms_unlock_logs'])
    def test_hotel_rooms_unlock_logs(self, data):
        """
        门店下所有房屋的开锁记录
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.hotel_rooms_unlock_logs(token=token, hotelCode=data['hotelCode'])

        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_hotel_rooms'])
    def test_hotel_rooms(self, data):
        """
        门店下属房屋列表查询
        :return:
        """
        token = self.adminweb.get_token()
        r = self.basic.hotel_rooms(token=token, hotelCode=data['hotelCode'], psbUnit=data['psbUnit'],
                                   turonoutCodeList=data['turonoutCodeList'], checkState=data['checkState'],
                                   pageNum=data['pageNum'], pageSize=data['pageSize'])

        assert r['message'] == 'SUCCESS'

#
# if __name__=="__main__":
#     pytest.main(['-s','-q','--alluredir','report/result','TestBasic.py'])
#     os.system("D:/software/allure-2.7.0/bin/allure.bat "
#               "generate "
#               "D:/PYproject/HDSP/test_case/report/result"
#               "-o "
#               "D:/PYproject/HDSP/test_case/report/html")
