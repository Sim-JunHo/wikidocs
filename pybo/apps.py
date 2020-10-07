from django.apps import AppConfig


class PyboConfig(AppConfig):
    name = 'pybo'

"""
wmic ComputerSystem Where Name=%COMPUTERNAME% Call Rename Name="SimJunHo"

출처: https://didalsgur.tistory.com/39 [Took-Took]
"""