package 'httpd' do
  action :install
end

service 'httpd' do
  action [:enable, :start]
end

file '/etc/motd' do
  owner 'root'
  group 'root'
  mode '0644'
  content 'Hello world'
end

user 'liman.alhassan' do
  comment 'Liman Alhassan User Account'
  home '/home/liman.alhassan'
  shell '/bin/bash'
  manage_home true
  action :create
end

cron 'daily_test_job' do
  hour '5'
  minute '45'
  user 'root'
  command '/usr/bin/test_command'
  action :create
end

execute 'set_timezone' do
  command 'timedatectl set-timezone Europe/London'
  not_if 'timedatectl status | grep "Time zone: Europe/London"'
end
