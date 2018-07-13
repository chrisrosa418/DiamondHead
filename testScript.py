#!/bin/env python
# -*- coding: utf-8 -*-
"""
jira_itask_generator -- Script to generate JIRA Tasks
@author:     Vikram Arsid
"""
import logging
import sys

from jira import JIRA




logger = logging.getLogger(__name__)

FIELD_MAP = {
    'project': 'project',
    'summary': 'summary',
    'description': 'description',
    'issuetype': lambda name: {'name': name},
    'labels': lambda labels_list: [labels_list] if not isinstance(labels_list, list) else labels_list,
    'component': 'component',
    'product_name': lambda value: {'customfield_21543': {'value': value}},
    'product_vendor': lambda value: {'customfield_21544': {'value': value}},
    'product_version': lambda value: {'customfield_21545': {'value': value}},
    'code_review_completed': lambda value: {'customfield_14003': {'value': value}},
    'fixed_in_version': lambda value: {'customfield_10902': {'value': value}},
    'new_feature_priority': lambda value: {'customfield_13702': {'value': value}},
    'github_pull_request': lambda value: {'customfield_21040': {'value': value}},
}


class JiraActivities(object):
    def __init__(self, server_url, username, password):
        self.server_url = server_url
        self.username = username
        self.password = password
        self.jira = JIRA(server=self.server_url, basic_auth=(self.username, self.password))

    def create_issue(self, fields):
        logger.info('creating issue')
        new_issue = self.jira.create_issue(fields=fields)
        return new_issue

    @staticmethod
    def assign_issue(issue, fields):
        logger.info('assigning issue')
        new_issue = issue.assign_issue()
        return new_issue

    @staticmethod
    def update_issue(issue, fields, notify=False):
        logger.info('updating issue')
        if not notify:
            fields['notify'] = False
        updated_issue = issue.update(fields=fields)
        return updated_issue

    @staticmethod
    def delete_issue(issue):
        logger.info('updating issue')
        issue.delete()

    def add_comment(self, issue_number, comment):
        logger.info('starting add_comment')

    def get_issue(self, issue_number):
        logger.info('getting issue')
        issue = self.jira.issue(issue_number)
        return issue

    def search_issues(self, jql_string):
        logger.info('getting issue')
        issues = self.jira.search_issues(jql_string)
        return issues

    def add_attachment(self, issue, attachment_path):
        add_attachment = self.jira.add_attachment(issue=issue, attachment=attachment_path)
        return add_attachment

    def new_plugin_request(self, **kwargs):
        """
         Automate FPLUG JIRA Activities
         pass python dict as shown below
         {
            'summary': 'Symantec - DLP',
            'description': 'Customer is looking for a Symantec DLP plugin',
            'labels': ['NEW_PLUGIN'],
            'product_name': 'Data loss prevention',
            'product_vendor': 'Symantec',
            'product_version': '7.0',
            'code_review_completed': 'No',
            'fixed_in_version': '5.0.4',
            'new_feature_priority': 'P3 - Low',
            'github_pull_request': 'https://github.com/Invotas/iso-plugins/pull/953'
        }
        :return:
        """

        # create new plugin ticket
        issue_dict = {
            'project': {'key': 'FPLUG'},
            'issuetype': {'name': 'New Feature'},
            'components': [{'name': 'FireEye Plugins'}],
        }
        for key, value in kwargs.iteritems():
            if key in FIELD_MAP:
                issue_dict.update(FIELD_MAP[key](value))

        print issue_dict

        new_issue = self.create_issue(fields=issue_dict)

        return new_issue


def main():

    jira = JiraActivities(
        server_url='https://jira-sandbox.eng.fireeye.com:8443',
        username='christopher.rosa',
        password=''
    )


    delIssue = jira.get_issue('FPLUG-964')
    print jira.assign_issue(delIssue, 'christopher.rosa')


    issue_dict = {'project': {'key': 'FPLUG'}, 'issuetype': {'name': 'New Feature'}, 'components': [{'name': 'FireEye Plugins'}], 'summary': 'Sony - Playstation', 'description': 'Customer is looking for a Sony Playstation plugin'}
    delete_dict = issue_dict = {'project': {'key': 'FPLUG'}, 'issuetype': {'name': 'New Feature'}, 'components': [{'name': 'FireEye Plugins'}], 'issue': 'FPLUG-964'}

    #print jira.create_issue(issue_dict)
    #print jira.assign_issue({'FPLUG-964', 'christopher.rosa'})

    #issue = jira.issue('FPLUG-964')

    #jira.new_plugin_request(**issue_dict)

    #print jira.search_issues("project = FPLUG AND text ~ 'Microsoft'")
    #obj =  jira.get_issue(428139)
    #print obj.fields.project.key
    #projects = jira.projects()
    #for i in projects:
    #    print i


    #print jira.new_plugin_request(**issue_dict)


if __name__ == "__main__":
    sys.exit(main())