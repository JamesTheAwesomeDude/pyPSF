import setuptools

setuptools.setup(
	name="pypsf",
	version="0.3.0b1",
	author="James Edington",
	author_email="james@ishygddt.xyz",
	description="Library for interacting with PC Screen Font files",
	packages=setuptools.find_packages(),
	classifiers=[
	 "Development Status :: 3 - Alpha",
	],
	include_package_data=True,
	install_requires=["Pillow"],
	entry_points={
	 'console_scripts': [
		"psf_extract=psf.util:psf2dir_entrypoint"
	 ],
	}
)
