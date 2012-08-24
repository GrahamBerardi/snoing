#!/usr/bin/env python
# Author P G Jones - 24/08/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base logger class, this saves information to file, but does not display to screen
import os

class Logger(object):
    """ Update with pacakages state change information, and convey information to a
    file.
    """

    def __init__(self, local, install):
        """ Save the file paths and setup the install folder file if needed."""
        self._local_file = local
        self._install_file = install
        if not os.path.exists(self._install_file):
            file_ = open(self._install_file, "w")
            file_.write( "## SNOING\nThis is a snoing install directory. Please alter only with snoing at %s" % __file__ )
            file_.close()
        if os.path.exists(self._local_file):
            os.remove(self._local_file)

    def package_registered(self, package_name):
        """ Notify that a package has been registered."""
        self._write_local("Package %s registered.\n" % package_name)

    def package_downloaded(self, package_name):
        """ Notify that a package has been downloaded."""
        self._write_local("Package %s downloaded.\n" % package_name)

    def package_installed(self, package_name):
        """ Notify that a package has been installed."""
        self._write_local("Package %s installed.\n" % package_name)
        self._write_install("Package %s installed.\n" % package_name)

    def package_removed(self, package_name):
        """ Notify that a package has been removed."""
        self._write_local("Package %s removed.\n" % package_name)
        self._write_install("Package %s removed.\n" % package_name)

    def package_updated(self, package_name):
        """ Notify that a package has been updated."""
        self._write_local("Package %s updated.\n" % package_name)
        self._write_install("Package %s updated.\n" % package_name)

    def info(self, info_message):
        """ Output some information."""
        self._write_local("%s\n" % info_message)

    def error(self, error_message):
        """ Notify that an error has occurred."""
        self._write_local("%s\n" % error_message)

    def _write_local(self, text):
        """ Write information to the local file."""
        file_ = open(self._local_file, "a")
        file_.write(text)
        file_.close()

    def _write_install(self, text):
        """ Write information to the local file."""
        file_ = open(self._install_file, "a")
        file_.write(text)
        file_.close()
