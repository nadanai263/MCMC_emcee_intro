import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MaxNLocator
import cycler as cycler


def plot1(x,y,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(8.27,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )

	f, axarr=plt.subplots()
	
	axarr.plot(x,y,'-')
	formatplot(axarr,xlabel,ylabel,legend,False,False,False,False,False,title)
	plt.title(title)
	plt.show()

def plot2(x,y,xobs,yobs,yerr,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(8.27,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )

	f, axarr=plt.subplots()
	
	axarr.plot(x,y,'-')
	axarr.errorbar(xobs,yobs,yerr=yerr,fmt='o')

	formatplot(axarr,xlabel,ylabel,legend,False,False,False,False,False,title)
	plt.show()

def plot3(x1,y1,x2,y2,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(18,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )

	f, axarr=plt.subplots(1,2)
	
	axarr[0].plot(x1,y1,'-')
	axarr[1].plot(x2,y2,'-')
	formatplot(axarr[0],'$y_{max}$',ylabel,legend,False,False,False,False,False,title)
	formatplot(axarr[1],'$K$',ylabel,legend,False,False,False,False,False,title)
	plt.show()

def plot4(x1,y1,x2,y2,samples,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(18,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )

	f, axarr=plt.subplots(1,2)
	axarrt1=axarr[0].twinx()
	axarrt2=axarr[1].twinx()

	axarr[0].plot(x1,y1,'-')
	axarrt1.hist(samples[:,0],bins=200,color='#0d76e8') #f55f4e red #0d76e8 blue

	axarr[1].plot(x2,y2,'-')
	axarrt2.hist(samples[:,1],bins=200,color='#0d76e8')
	formatplot(axarr[0],'$y_{max}$',ylabel,legend,False,False,False,False,False,title)

	formatplot(axarr[1],'$K$',False,legend,False,False,False,False,False,title)
	plt.show()

def plot5(x,y,xobs,yobs,yerr,samples,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(8.27,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )


	f, axarr=plt.subplots()
	
	axarr.plot(x,y,'-')
	axarr.errorbar(xobs,yobs,yerr=yerr,fmt='o')

	xmod=np.linspace(0,10,50)
	for ymax,K in samples[np.random.randint(len(samples), size=20)]:
		ymod=ymax*xmod/(xmod+K)
		axarr.plot(xmod,ymod,'k-',label='_nolegend_',alpha=0.1)

	formatplot(axarr,xlabel,ylabel,legend,False,False,False,False,False,title)
	plt.show()


def formatplot(ax,xlabel,ylabel,legend,xlim,ylim,logx,logy,logxy,title):
	my_dpi=150
	
	######### SET AXES LIMITS #########

	if xlim!=False:
		ax.set_xlim([0,35])
	if ylim!=False:
		ax.set_ylim([0.05,25])

	######### SET TICK VALUES #########

	ax.tick_params(axis='both',pad=10)
#	ax.set_xticks([0,2e-5,4e-5,6e-5])
#	ax.set_yticks([0,2,4,6,8])

	######### SET TITLES AND LABLES #########

	if title!=False:
		ax.set_title(title)
	if xlabel!=False:
		ax.set_xlabel(xlabel, labelpad=12)
	if ylabel!=False:
		ax.set_ylabel(ylabel, labelpad=12)

	######### SET LINE THICKNESSES #########

#	ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter("%1.e"))
#	ax.axhline(linewidth=2, color='k')      
#	ax.axvline(linewidth=2, color='k')
	ax.spines['bottom'].set_linewidth(2)
	ax.spines['top'].set_linewidth(2)
	ax.spines['left'].set_linewidth(2)
	ax.spines['right'].set_linewidth(2) 

	######### SET TICKS #########

	if logx==True:

		ax.set_xscale("log")

	elif logy==True:

		ax.set_yscale("log")

	elif logxy==True:

		ax.set_xscale("log")
		ax.set_yscale("log")

	else:
		minorLocatorx=AutoMinorLocator(2) # Number of minor intervals per major interval
		minorLocatory=AutoMinorLocator(2)
		ax.xaxis.set_minor_locator(minorLocatorx)
		ax.yaxis.set_minor_locator(minorLocatory)

	ax.tick_params(which='major', width=2, length=8, pad=9, direction='in')
	ax.tick_params(which='minor', width=2, length=4, pad=9, direction='in')


	######### CALL LEGEND #########

	if legend==True:
		ax.legend(loc='best', fontsize=22,numpoints=1)



def plottraces(data,parameternames,parametertruths,nwalkers,niterations,save=1):

	numberofplots=data.shape[1]

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(11.7,8.3)} #figure size in inches. A4=11.7x8.3. 
	font_options={'size':'6','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)
#	fig=plt.figure(); ax=fig.add_subplot(1,1,1)

	######### CALL PLOTS #########

	if numberofplots>1:
		f, axarr=plt.subplots(numberofplots)
		for i in range(0,numberofplots):
			for j in range(1,nwalkers+1):
				axarr[i].plot(np.arange(niterations),data[niterations*j-niterations:niterations*j,i],'k-',lw=0.5)
			if parametertruths!=[]:
				axarr[i].axhline(parametertruths[i], color="#888888", lw=2)
			formatplottrace(axarr[i],parameternames[i])
	else:
		f, axarr=plt.subplots()
		for i in range(1,nwalkers+1):
			axarr.plot(np.arange(niterations),data[niterations*i-niterations:niterations*i],'k-',lw=0.5)
		if parametertruths!=[]:
			axarr.axhline(parametertruths[0], color="#888888", lw=2)
		formatplottrace(axarr,parameternames[0])


	######### SAVE PLOT #########
	if save==True:
		print()
		print('Saving file...')
		print()
		plt.savefig('plots/trace.png',dpi=my_dpi,bbox_inches='tight')
	else:
		plt.show()

def formatplottrace(ax,parametername):

	######### SET TICK VALUES #########

	ax.tick_params(axis='both',pad=10)
#	ax.set_xticks([0,2e-5,4e-5,6e-5])
#	ax.set_yticks([0,2,4,6,8])

	######### SET TITLES AND LABLES #########

	#ax.set_title('Plot title')
#	ax.set_xlabel('x', labelpad=12)
	ax.set_ylabel(parametername, labelpad=12)

	######### SET LINE THICKNESSES #########

#	ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter("%1.e"))
#	ax.axhline(linewidth=2, color='k')      
#	ax.axvline(linewidth=2, color='k')
	ax.spines['bottom'].set_linewidth(1)
	ax.spines['top'].set_linewidth(1)
	ax.spines['left'].set_linewidth(1)
	ax.spines['right'].set_linewidth(1) 

	######### SET TICKS #########

	minorLocatorx=AutoMinorLocator(2) # Number of minor intervals per major interval
	minorLocatory=AutoMinorLocator(2)
	ax.xaxis.set_minor_locator(minorLocatorx)
	ax.yaxis.set_minor_locator(minorLocatory)

	ax.tick_params(which='major', width=1, length=8, pad=9)
	ax.tick_params(which='minor', width=1, length=4, pad=9)


	######### CALL LEGEND #########

#	ax.legend(loc='best', fontsize=22,numpoints=1)
