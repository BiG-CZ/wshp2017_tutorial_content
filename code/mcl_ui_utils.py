
import sys
import os
import getpass
from IPython.display import display, HTML
import ipywidgets as widgets
from ipywidgets import Layout, HBox, Label
import numpy as np
from odm2api.ODM2.models import *

def getSecurePassword():
    u = getpass.getuser('Enter the ODM2 username')
    return u


def ODM2LoginPrompt():
    container = widgets.Box() # would be nice If I could get a container to hold the 
    # user name and password prompt, getpass doesn't seem to play well with the other 
    # widgets though
    username_text = widgets.Text(
        value='', placeholder='Enter username',
        description='', disabled=False)
    username_output_text = widgets.Text(
        value='', placeholder='Enter username',
        description='Username',disabled=False)
    database_address_text = widgets.Text(
        value='', placeholder='Enter database address',
        description='',disabled=False)
    database_address_output_text = widgets.Text(
        value='',placeholder='Enter database address',
        description='database address',disabled=False)
    database_text = widgets.Text(
        value='', placeholder='Enter database name',
        description='', disabled=False)
    database_output_text = widgets.Text(
        value='', placeholder='Enter database name',
        description='database name', disabled=False)
    def bind_username_to_output(sender):
        username_output_text.value = username_text.value
    def bind_database_address_to_output(sender):
        database_address_output_text.value = database_address_text.value
    def bind_database_to_output(sender):
        database_output_text.value = database_text.value     

    def login(sender):
        #print('Database address : %s, Username: %s, database name: %s' % (
        #    database_address_text.value, username_text.value, database_text.value))
        container.close()    

    username_text.on_submit(bind_username_to_output)
    login_btn = widgets.Button(description="Login")
    login_btn.on_click(login)
    container.children = [username_text,database_address_text, database_text, login_btn]
    #container
    return container

def annotationContainer():
    
    annotation_text = widgets.Text(
        value='', placeholder='Enter an annotation',
        description='annotation', disabled=False)
    annotation_output_text = widgets.Text(
        value='', placeholder='Enter an annotation',
        description='',disabled=False)
    annotation_code_text = widgets.Text(
        value='', placeholder='Enter an annotation code or leave blank',
        description='annotation code', disabled=False)
    annotation_code_output_text = widgets.Text(
        value='', placeholder='anotation code',
        description='',disabled=False)
    def bind_annotation_to_output(sender):
        annotation_output_text.value = annotation_text.value
    def bind_annotation_code_to_output(sender):
        annotation_code_output_text.value = annotation_code_text.value

    def submit(sender):
        print('Annoatation : %s, Annotation Code: %s' % (
            annotation_text.value, annotation_code_text.value))
        container.close()
    container = widgets.Box()
    submit_btn = widgets.Button(description="Submit")
    submit_btn.on_click(submit)
    container.children = [annotation_text,annotation_code_text, submit_btn]
    return container

def startDateEndDateContainer():
    
    start_date_text = widgets.Text(
        value='', placeholder='2017-01-01',
        description='start date', disabled=False)
    start_date_output_text = widgets.Text(
        value='', placeholder='2017-01-01',
        description='',disabled=False)
    end_date_text = widgets.Text(
        value='', placeholder='2017-01-06',
        description='end date', disabled=False)
    end_date_output_text = widgets.Text(
        value='', placeholder='2017-01-06',
        description='',disabled=False)
    def bind_start_date_to_output(sender):
        start_date_output_text.value = start_date_text.value
    def bind_end_date_to_output(sender):
        end_date_output_text.value = end_date_text.value

    def submit(sender):
        print('start date : %s, end date: %s' % (
            start_date_text.value, end_date_text.value))
        container.close()
    container = widgets.Box()
    submit_btn = widgets.Button(description="Submit")
    submit_btn.on_click(submit)
    container.children = [start_date_text,end_date_text, submit_btn]
    return container


def dataqualityWidget(DBSession):
    dataquality_code =  DBSession.query(CVQualityCode)
    def print_dataquality_code_name(code):
        print(code)
    def on_change(change):
        print(change['new'])
    dqtids = []
    dqtnames = {}
    for dq in dataquality_code:
        dqtids.append(dq.Name)
        namestr = str(dq.Name   + " - " + dq.Term)
        dqtnames[namestr] = dq.Name
    dataquality_codeWidget = widgets.Dropdown(options=dqtnames, layout=Layout(width='50%', height='30px'))
    dataquality_codeWidget.label = ''
    dqwidget = widgets.interactive(print_dataquality_code_name,code=dataquality_codeWidget)
    dqwidget.observe(on_change)
    #label = Label('data quality ',layout=Layout(height='30px'))
    #box = HBox([label, dataquality_codeWidget]) #dqwidget
    return dataquality_codeWidget, dqwidget

def actionWidget(DBSession):

    #featureaction = 1700
    actions = DBSession.query(Actions).filter_by(ActionTypeCV = 'Observation') 
    actionids = []
    actionnames = {}

    def print_action_name(action):
        print(action)
    def on_change(change):
        print(change['new'])

    for a in actions:
        #print(r.ResultID)
        actionids.append(str(a.ActionID))
        #action_type=read.CVActionType(name=a.ActionTypeCV) 
        method =  DBSession.query(Methods).filter_by(MethodID =a.MethodID).one()
        #detailr = read.getDetailedResultInfo(resultTypeCV = 'Time series coverage',resultID=r.ResultID)
        namestr = str(method.MethodCode   + "- Begin date - " + str(a.BeginDateTime))
        actionnames[namestr]=  str(a.ActionID)
        #print(detailr.Methods)
    print(actionids)
    actionWidget = widgets.Dropdown(options=actionnames, layout=Layout(width='50%', height='30px'))
    awidget = widgets.interactive(print_action_name,action=actionWidget)
    awidget.observe(on_change)
    return actionWidget, awidget

def actionWidgetNotPulse(DBSession):

    #featureaction = 1700
    dsrs = DBSession.query(DataSetsResults).filter_by(DataSetID=17)
    dsrids = []
    for dsr in dsrs:
        dsrids.append(dsr.ResultID)
    results =  DBSession.query(TimeSeriesResults).filter(~TimeSeriesResults.ResultID.in_(dsrids))
    featureactions = DBSession.query(FeatureActions).join(Results).filter(~Results.ResultID.in_(dsrids))
    faids =[]
    for fa in featureactions:
        faids.append(fa.FeatureActionID)
    #actions = DBSession.query(Actions).filter_by(ActionTypeCV = 'Observation'
    #                                            ).join(FeatureActions).filter(FeatureActions.FeatureActionID.in_(faids))

    actionids=[34, 35,21,22,8] #34,
    actions = DBSession.query(Actions).filter(Actions.ActionID.in_(actionids))
    actionids = []
    actionnames = {}

    def print_action_name(action):
        print(action)
    def on_change(change):
        print(change['new'])

    for a in actions:
        #print(r.ResultID)
        actionids.append(str(a.ActionID))
        #action_type=read.CVActionType(name=a.ActionTypeCV) 
        method =  DBSession.query(Methods).filter_by(MethodID =a.MethodID).one()
        #detailr = read.getDetailedResultInfo(resultTypeCV = 'Time series coverage',resultID=r.ResultID)
        namestr = str(method.MethodCode   + "- Begin date - " + str(a.BeginDateTime))
        actionnames[namestr]=  str(a.ActionID)
        #print(detailr.Methods)
    print(actionids)
    actionWidget = widgets.RadioButtons(options=actionnames) #layout=Layout(width='50%',min_width='50%'), height='30px'
    awidget = widgets.interactive(print_action_name,action=actionWidget)
    awidget.observe(on_change)
    return actionWidget, awidget

def resultWidget(read, actionid):
    
    results = read.getResults(actionid=actionid)
    resultids = []
    resultnames = {}

    def print_result_name(result):
        print(result)
    def on_change(change):
        print(change['new'])

    for r in results:
        #print(r.ResultID)
        resultids.append(str(r.ResultID))
        detailr = read.getDetailedResultInfo(resultTypeCV = 'Time series coverage',resultID=r.ResultID)
        for detail in detailr:
            namestr = str(str(detail.resultID) + "- " + detail.samplingFeatureCode + "- " + detail.methodCode + "- "+ detail.variableCode + "- " + detail.unitsName)
            resultnames[namestr]=  detail.resultID
        #print(detailr.Methods)
    print(resultids)
    resultWidget = widgets.RadioButtons(options=resultnames)
    rwidget = widgets.interactive(print_result_name,result=resultWidget)
    rwidget.observe(on_change)
    return resultWidget, rwidget
