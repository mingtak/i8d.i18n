# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from i8d.i18n.testing import I8D_I18N_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that i8d.i18n is properly installed."""

    layer = I8D_I18N_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if i8d.i18n is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('i8d.i18n'))

    def test_browserlayer(self):
        """Test that II8DI18NLayer is registered."""
        from i8d.i18n.interfaces import II8DI18NLayer
        from plone.browserlayer import utils
        self.assertIn(II8DI18NLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = I8D_I18N_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['i8d.i18n'])

    def test_product_uninstalled(self):
        """Test if i8d.i18n is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('i8d.i18n'))

    def test_browserlayer_removed(self):
        """Test that II8DI18NLayer is removed."""
        from i8d.i18n.interfaces import II8DI18NLayer
        from plone.browserlayer import utils
        self.assertNotIn(II8DI18NLayer, utils.registered_layers())
