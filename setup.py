from distutils.core import setup
import setup_translate


setup(name='enigma2-plugin-extensions-sundtekcontrolcenter',
		version='20160419-1',
		author='giro77, Sundtek, Dimitrij',
		author_email='dima-73@inbox.lv',
		package_dir={'Extensions.SundtekControlCenter': 'src'},
		packages=['Extensions.SundtekControlCenter'],
		package_data={'Extensions.SundtekControlCenter': ['images/*.png', '*.sh', '*.png']},
		description='control sundtek usb stick from enigma2',
		cmdclass=setup_translate.cmdclass,
	)
