insert overwrite TABLE top_complaint_states 
select state,count(*) cnt
from stage_complaints
group by state
order by cnt desc
limit 20;