import requests
import os
from api.admin_web import Adminweb


class Basic(Adminweb):

    def otainfo_list(self, token, **kwargs):
        """网约房平台信息列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/otainfo/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def otainfo_detail(self, token, otaCode, **kwargs):
        """网约房平台信息详情"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        params = {'otaCode': otaCode}
        url = Adminweb.ucenter_host + '/server/otainfo/detail'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def otainfo_export(self, token, **kwargs):
        """网约房平台导出"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/otainfo/export'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def employee_employeeList(self, token, **kwargs):
        """从业人员管理列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/employee/employeeList'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def employee_personInfo(self, token, cardNum, **kwargs):
        """从业人员管理详情"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/employee/personInfo/' + cardNum
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def employee_employeeHotelInfo(self, token, cardNum, **kwargs):
        """从业人员详情-门店"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/employee/employeeHotelInfo/' + cardNum
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def employee_employeeRoomInfo(self, token, cardNum, **kwargs):
        """从业人员详情-房屋"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/employee/employeeRoomInfo/' + cardNum
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def employee_exportExcel(self, token, **kwargs):
        """导出--从业人员信息列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/employee/exportExcel'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_list(self, token, **kwargs):
        """房屋列表查询"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_detail(self, token, roomCode, **kwargs):
        """房屋详情查询"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        params = {'roomCode': roomCode}
        url = Adminweb.ucenter_host + '/server/room/detail'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def room_update(self, token, **kwargs):
        """房屋编辑"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/update'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_unlock_logs(self, token, **kwargs):
        """查询房屋下的开锁记录"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/unlock/logs'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_del(self, token, **kwargs):
        """房屋删除"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/del'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_check_list(self, token, **kwargs):
        """查询房屋核检查记录列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/check/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_check_detail(self, token, iidd, **kwargs):
        """查询房屋核检查记录详情"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        params = {'iidd': iidd}
        url = Adminweb.ucenter_host + '/server/room/check/detail'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def room_checkstate_reset(self, token, roomCode, checkId, reason, **kwargs):
        """重置房屋核查状态"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        params = {'roomCode': roomCode, 'checkId': checkId, 'reason': reason}
        url = Adminweb.ucenter_host + '/server/room/checkstate/reset'
        r = requests.post(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def room_merge(self, token, **kwargs):
        """合并房屋"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/merge'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_split(self, token, **kwargs):
        """拆分房屋"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/split'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def hotel_list_export(self, token, **kwargs):
        """门店列表信息导出"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/hotel/list/export'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_list_export(self, token, **kwargs):
        """房屋列表信息导出"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/list/export'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def room_childs(self, token, roomCode, **kwargs):
        """子房屋列表查询"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }

        params = {'roomCode': roomCode}
        url = Adminweb.ucenter_host + '/server/room/childs'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def room_uploadimg(self, token, files, iidd, roomCode):
        """房屋图片上传"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        body = {
            'iidd': iidd,
            'roomCode': roomCode,
            'files': (os.path.basename(files), open(files, 'rb'), 'image/jpg')
        }
        url = Adminweb.ucenter_host + '/server/room/uploadimg'
        r = requests.post(url=url, headers=headers, files=body)
        self.format(r)
        return r.json()

    def calendar_hotelCalendar(self, token, hotelCode, year, month):
        """门店旅客入住日历"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        params = {
            'hotelCode': hotelCode,
            'year': year,
            'month': month
        }
        url = Adminweb.ucenter_host + '/server/calendar/hotelCalendar'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def street_list(self, token, **kwargs):
        """获取街路巷列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/room/street/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def hotel_list(self, token, **kwargs):
        """门店列表查询"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/hotel/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def hotel_detail(self, token, hotelCode, **kwargs):
        """门店详情查询"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        params = {"hotelCode": hotelCode}
        url = Adminweb.ucenter_host + '/server/hotel/detail'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def hotel_merchant_update(self, token, **kwargs):
        """门店信息编辑"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/hotel/merchant/update'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def hotel_rooms_unlock_logs(self, token, **kwargs):
        """门店下所有房屋的开锁记录"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/hotel/rooms/unlock/logs'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def hotel_rooms(self, token, **kwargs):
        """门店下属房屋列表查询"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token,
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/hotel/rooms'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()
