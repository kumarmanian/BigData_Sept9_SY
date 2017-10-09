select product,
sub_product,
issue,
sub_issue,
company,
state,
zip_code,
submitted_via,
TO_DATE(from_unixtime(UNIX_TIMESTAMP(date_sent_to_company, 'MM/dd/yyyy'))) date_sent_to_company,
timely_response,
consumer_disputed,
complaint_id,
substr(date_received,7,4) year,substr(date_received,1,2) month,substr(date_received,4,2) day 
from raw_complaints_tab
where (state is not null and  length(state) != 0)
and (zip_code is not null and length(zip_code) != 0 and regexp_extract (zip_code,'(.*?)(XX)',2) != 'XX');