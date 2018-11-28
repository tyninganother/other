# encoding=utf-8
import urllib
import urllib2
import StringIO

# -*- coding: UTF-8 -*-
import mimetypes
import mimetools
import itertools


class MultiPartForm():
    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()

    def add_field(self, name, value):
        """添加field数据到form表单"""
        self.form_fields.append((name, value))

    def add_file(self, fieldname, filename, file_obj, mimetype=None):
        """添加文件到表单"""
        if not mimetype:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, file_obj.read()))

    def __str__(self):
        """拼接form报文"""
        parts = []
        part_boundary = "--%s" % self.boundary

        # 添加fields
        parts.extend(
            [part_boundary,
             'Content-Disposition: form-data; name="%s"' % name,
             '',
             value, ] for name, value in self.form_fields
        )

        # 添加要上传的files
        parts.extend(
            [part_boundary,
             'Content-Disposition: file; name="%s"; filename="%s"' % (field_name, filename),
             'Content-Type: %s' % content_type,
             '',
             body, ] for field_name, filename, content_type, body in self.files
        )

        # 压平parts添加boundary终止符
        flattened = list(itertools.chain(*parts))
        flattened.append('--%s--' % self.boundary)
        flattened.append('')
        return '\r\n'.join(flattened)


# POST请求的目标URL
url = "http://10.10.1.68:8080/api/3.0/appstaore/crashFileUpload"

form = MultiPartForm()
form.add_field('params', '{}')
form.add_field('from', 'W')

# form.add_file('file', '/Users/haining/test/2018090920190099-eee.txt', file_obj=StringIO('urllib2 file upload.'))
form.add_file('file', 'file',open('/Users/haining/test/2018090920190099-eee.txt'))

request = urllib2.Request(url)
body = str(form)
request.add_header('Content-type', 'multipart/form-data; boundary=%s' % form.boundary)
request.add_header('Content-length', len(body))
request.add_data(body)

print
print 'Request'
print request.get_data()

print
print 'Response'
print urllib2.urlopen(request).read()
