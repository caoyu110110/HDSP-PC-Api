import requests
import os
from api.admin_web import Adminweb


class Guest(Adminweb):

    def overseaGuest_reverse_overseaGuestList(self, token, **kwargs):
        """境外旅客预定列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/overseaGuest/reverse/overseaGuestList'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def overseaGuest_reverse_overseaGuestInfoById(self, token, guestCode, **kwargs):
        """境外旅客预定人员的个人信息"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/overseaGuest/reverse/overseaGuestInfoById/' + guestCode
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def overseaGuest_reverse_overseaGuestRecordById(self, token, guestCode, **kwargs):
        """境外旅客预定记录"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/overseaGuest/reverse/overseaGuestRecordById/' + guestCode
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def overseaGuest_reverse_exportExcel(self, token, **kwargs):
        """境外旅客预定信息导出"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/overseaGuest/reverse/exportExcel'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def overseaGuest_checkIn_overseaGuestListl(self, token, **kwargs):
        """境外旅客入住列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/overseaGuest/checkIn/overseaGuestList'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def overseaGuest_checkIn_overseaGuestInfoById(self, token, guestCode, **kwargs):
        """境外旅客入住人员的个人信息"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/overseaGuest/checkIn/overseaGuestInfoById/' + guestCode
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def overseaGuest_checkIn_overseaGuestRecordById(self, token, guestCode, **kwargs):
        """境外旅客入住记录"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/overseaGuest/checkIn/overseaGuestRecordById/' + guestCode
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def overseaGuest_checkIn_exportExcel(self, token, **kwargs):
        """境外旅客入住信息导出"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/overseaGuest/checkIn/exportExcel'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localGuest_checkIn_localGuestList(self, token, **kwargs):
        """境内旅客入住列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/localGuest/checkIn/localGuestList'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localGuest_checkIn_localGuestById(self, token, guestCode, **kwargs):
        """境内旅客入住人员的个人信息"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/localGuest/checkIn/localGuestById/' + guestCode
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localGuest_checkIn_localGuestCheckInById(self, token, guestCode, **kwargs):
        """境内旅客入住记录"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/localGuest/checkIn/localGuestCheckInById/' + guestCode
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localGuest_checkIn_exportExcel(self, token, **kwargs):
        """境内旅客入住信息导出为excel"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/localGuest/checkIn/exportExcel'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localGuest_reverse_localGuestList(self, token, **kwargs):
        """境内旅客预定列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/localGuest/reverse/localGuestList'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localGuest_reverse_localGuestReverseById(self, token, guestCode, **kwargs):
        """境内旅客预定记录"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/localGuest/reverse/localGuestReverseById/' + guestCode
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localGuest_reverse_localGuestById(self, token, guestCode, **kwargs):
        """境内旅客预定人员的个人信息"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/localGuest/reverse/localGuestById/' + guestCode
        r = requests.get(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def local_Guestreverse_exportExcel(self, token, **kwargs):
        """境内旅客预定信息导出为excel"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/localGuest/reverse/exportExcel'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localguest_list(self, token, **kwargs):
        """境内旅客个人信息列表"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/localguest/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localguest_detail(self, token, cardNum, **kwargs):
        """境内旅客个人信息详情"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        params = {'cardNum': cardNum}
        url = Adminweb.ucenter_host + '/server/localguest/detail'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def localguest_export(self, token, **kwargs):
        """境内旅客个人信息列表导出"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/localguest/export'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def localguest_history(self, token, cardNum, **kwargs):
        """境内旅客个人信息详情"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        params = {'cardNum': cardNum}
        url = Adminweb.ucenter_host + '/server/localguest/history'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()

    def localguest_roommate(self, token, cardNum, **kwargs):
        """境内旅客个人信息同住人"""
        headers = {
            "Content-Type": Adminweb.Content_Type,
            "Authorization": token

        }
        params = {'cardNum': cardNum}
        url = Adminweb.ucenter_host + '/server/localguest/history'
        r = requests.get(url=url, headers=headers, params=params)
        self.format(r)
        return r.json()
