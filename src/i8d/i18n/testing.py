# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import i8d.i18n


class I8DI18NLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=i8d.i18n)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'i8d.i18n:default')


I8D_I18N_FIXTURE = I8DI18NLayer()


I8D_I18N_INTEGRATION_TESTING = IntegrationTesting(
    bases=(I8D_I18N_FIXTURE,),
    name='I8DI18NLayer:IntegrationTesting'
)


I8D_I18N_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(I8D_I18N_FIXTURE,),
    name='I8DI18NLayer:FunctionalTesting'
)


I8D_I18N_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        I8D_I18N_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='I8DI18NLayer:AcceptanceTesting'
)
