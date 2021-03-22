import pytest

from api.baseapi import BaseApi
from api.guest import Guest
from api.admin_web import Adminweb


class TestGuest:
    data = BaseApi.yaml_load('../yaml_data/test_guest.yaml')

    def setup(self):
        self.adminweb = Adminweb()
        self.guest = Guest()

    def test_overseaGuest_reverse_overseaGuestList(self):
        """
        境外旅客预定列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.overseaGuest_reverse_overseaGuestList(token=token)
        assert r['message'] == 'SUCCESS'

    def test_overseaGuest_reverse_overseaGuestInfoById(self):
        """
        境外旅客预定人员的个人信息
        :return:
        """
        token = self.adminweb.get_token()
        guestCode = self.guest.overseaGuest_reverse_overseaGuestList(token=token)['data'][0]['guestCode']
        r = self.guest.overseaGuest_reverse_overseaGuestInfoById(token=token, guestCode=guestCode)
        assert r['message'] == 'SUCCESS'

    def test_overseaGuest_reverse_overseaGuestRecordById(self):
        """
        境外旅客预定人员的个人信息
        :return:
        """
        token = self.adminweb.get_token()
        guestCode = self.guest.overseaGuest_reverse_overseaGuestList(token=token)['data'][0]['guestCode']
        r = self.guest.overseaGuest_reverse_overseaGuestRecordById(token=token, guestCode=guestCode)
        assert r['message'] == 'SUCCESS'

    def test_overseaGuest_reverse_exportExcel(self):
        """
        境外旅客预定信息导出
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.overseaGuest_reverse_exportExcel(token=token)
        assert r['message'] == 'SUCCESS'

    def test_overseaGuest_checkIn_overseaGuestListl(self):
        """
        境外旅客入住列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.overseaGuest_checkIn_overseaGuestListl(token=token)
        assert r['message'] == 'SUCCESS'

    def test_overseaGuest_checkIn_overseaGuestInfoById(self):
        """
        境外旅客入住人员的个人信息
        :return:
        """
        token = self.adminweb.get_token()
        guestCode = self.guest.overseaGuest_checkIn_overseaGuestListl(token=token)['data'][0]['guestCode']
        r = self.guest.overseaGuest_checkIn_overseaGuestInfoById(token=token, guestCode=guestCode)
        assert r['message'] == 'SUCCESS'

    def test_overseaGuest_checkIn_overseaGuestRecordById(self):
        """
        境外旅客入住人员的个人信息
        :return:
        """
        token = self.adminweb.get_token()
        guestCode = self.guest.overseaGuest_checkIn_overseaGuestListl(token=token)['data'][0]['guestCode']
        r = self.guest.overseaGuest_checkIn_overseaGuestRecordById(token=token, guestCode=guestCode)
        assert r['message'] == 'SUCCESS'

    def test_overseaGuest_checkIn_exportExcel(self):
        """
        境外旅客入住信息导出
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.overseaGuest_checkIn_exportExcel(token=token)
        assert r['message'] == 'SUCCESS'

    def test_localGuest_checkIn_localGuestList(self):
        """
        境内旅客入住列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.localGuest_checkIn_localGuestList(token=token)
        assert r['message'] == 'SUCCESS'

    def test_localGuest_checkIn_localGuestById(self):
        """
        境内旅客入住人员的个人信息
        :return:
        """
        token = self.adminweb.get_token()
        guestCode = self.guest.localGuest_checkIn_localGuestList(token=token)['data'][3]['guestCode']
        r = self.guest.localGuest_checkIn_localGuestById(token=token, guestCode=guestCode)
        assert r['message'] == 'SUCCESS'

    def test_localGuest_checkIn_localGuestCheckInById(self):
        """
        境内旅客入住记录
        :return:
        """
        token = self.adminweb.get_token()
        guestCode = self.guest.localGuest_checkIn_localGuestList(token=token)['data'][3]['guestCode']
        r = self.guest.localGuest_checkIn_localGuestCheckInById(token=token, guestCode=guestCode)
        assert r['message'] == 'SUCCESS'

    def test_localGuest_checkIn_exportExcel(self):
        """
        境内旅客入住信息导出为excel
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.localGuest_checkIn_exportExcel(token=token)
        assert r['message'] == 'SUCCESS'

    def test_localGuest_reverse_localGuestList(self):
        """
        境内旅客预定列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.localGuest_reverse_localGuestList(token=token)
        assert r['message'] == 'SUCCESS'

    def test_localGuest_reverse_localGuestReverseById(self):
        """
        境内旅客预定记录
        :return:
        """
        token = self.adminweb.get_token()
        guestCode = self.guest.localGuest_reverse_localGuestList(token=token)['data'][5]['guestCode']
        r = self.guest.localGuest_reverse_localGuestReverseById(token=token, guestCode=guestCode)
        assert r['message'] == 'SUCCESS'

    def test_localGuest_reverse_localGuestById(self):
        """
        境内旅客预定人员的个人信息
        :return:
        """
        token = self.adminweb.get_token()
        guestCode = self.guest.localGuest_reverse_localGuestList(token=token)['data'][5]['guestCode']
        r = self.guest.localGuest_reverse_localGuestById(token=token, guestCode=guestCode)
        assert r['message'] == 'SUCCESS'

    def test_local_Guestreverse_exportExcel(self):
        """
        境内旅客预定信息导出为excel
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.local_Guestreverse_exportExcel(token=token)
        assert r['message'] == 'SUCCESS'

    def test_localGuest_checkIn_localGuestList(self):
        """
        境内旅客个人信息列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.localGuest_checkIn_localGuestList(token=token)
        assert r['message'] == 'SUCCESS'

    def test_localguest_list(self):
        """
        境内旅客个人信息列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.localguest_list(token=token)
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_localguest_detail'])
    def test_localguest_detail(self, data):
        """
        境内旅客个人信息详情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.localguest_detail(token=token, cardNum=data['cardNum'])
        assert r['message'] == 'SUCCESS'

    def test_localguest_export(self):
        """
        境内旅客个人信息列表导出
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.localguest_export(token=token)
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_localguest_history'])
    def test_localguest_history(self, data):
        """
        境内旅客个人信息详情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.guest.localguest_history(token=token, cardNum=data['cardNum'])
        assert r['message'] == 'SUCCESS'
