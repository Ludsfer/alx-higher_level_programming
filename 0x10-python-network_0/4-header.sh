#!/bin/bash
# send a GET to URL. display X-School-User-Id sent with the value 98
curl - sH "X-HolbertonSchool-User-Id: 98" "${1}
