class SleepsController < ApplicationController
    skip_before_action :verify_authenticity_token, only: [:show]
    before_action :set_kerberos, :authenticate_kerberos
    before_action :authenticate_user!, only: [:edit, :create, :confirm]

    require 'net/https'
    require 'uri'
    require 'json'
    
    def index
        today = Date.today
        @year = today.year
        @month = today.month
        @day = today.day
        first_day = today.beginning_of_month
        @first_wday = first_day.wday
        end_day = today.end_of_month
        @end_wday = end_day.wday
        @date_list = (first_day.day..end_day.day).to_a
        @un_schedules = []
        for i in @date_list do
            date = format("%04d-%02d-%02d",@year, @month, i)
            usl = UndecidedSchedule.find_by(user_id: @kerbero.left_user_id, date: date)
            usc = UndecidedSchedule.find_by(user_id: @kerbero.center_user_id, date: date)
            usr = UndecidedSchedule.find_by(user_id: @kerbero.right_user_id, date: date)
            @un_schedules.push([])
            @un_schedules[i-1].push(usl)
            @un_schedules[i-1].push(usc)
            @un_schedules[i-1].push(usr)
        end
    end

    def edit
        today = Date.today
        @year = today.year
        @month = today.month
        @day = today.day
        first_day = today.beginning_of_month
        @first_wday = first_day.wday
        end_day = today.end_of_month
        @end_wday = end_day.wday
        @date_list = (first_day.day..end_day.day).to_a
        @un_schedules = []
        for i in @date_list do
            date = format("%04d-%02d-%02d",@year, @month, i)
            us = UndecidedSchedule.find_by(user_id: current_user.id, date: date)
            @un_schedules.push(us)
        end
    end

    def create
        if params[:date].blank?
            redirect_to kerberos_sleep_path
        else
            if (params[:hour1].to_i > -1 && params[:hour2].to_i > -1) && ( params[:hour1].to_i > params[:hour2].to_i || ( params[:hour1].to_i == params[:hour2].to_i && params[:minute1].to_i > params[:minute2].to_i ) )
                # ?????????????????????????????????????????????
                redirect_to kerberos_sleep_edit_path
            elsif params[:hour1].to_i < 0 || params[:hour2].to_i < 6 || params[:hour1].to_i > 23 || params[:hour2].to_i > 31 || ![0,10,20,30,40,50].include?(params[:minute1].to_i) || ![0,10,20,30,40,50].include?(params[:minute2].to_i)
                # ??????????????????????????????????????????
                redirect_to kerberos_sleep_edit_path
            else
                us = UndecidedSchedule.find_by(date: params[:date], user_id: current_user.id)
                if us.blank?
                    us = UndecidedSchedule.new
                elsif us.is_confirmed
                    # ??????????????????????????????????????????
                    redirect_to kerberos_sleep_edit_path
                end
                us.date = params[:date]
                us.user_id = current_user.id
                us.start_time = format("%02d:%02d",params[:hour1].to_i,params[:minute1].to_i)
                us.end_time = format("%02d:%02d",params[:hour2].to_i,params[:minute2].to_i)
                us.save
            end
            redirect_to kerberos_sleep_edit_path
        end
    end

    def show
        if params[:date].blank?
            redirect_to kerberos_sleep_path
        else
            # ?????????URL????????????
            uri = URI.parse("http://20.78.224.237:8000/api/get_rest_schedules/")
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = false
            http.verify_mode = OpenSSL::SSL::VERIFY_NONE
        
            data = JSON.generate({:start_date => params[:date], :kerbero_id => @kerbero.id})
            render json: data
        
            # http.start do
            #   req = Net::HTTP::Post.new(uri.path)
            #   req.set_form_data(body: data)
            #   response = http.request(req)
            # end
            # render json: {response.code => response.body}.to_json
        end
    end

    def confirm
        un_schedules = UndecidedSchedule.where(user_id: current_user.id, is_confirmed: false)
        shift = []
        un_schedules.each do |u|
            hash = {:date => u.date, :request => true, :start_time => u.start_time, :end_time => u.end_time}
            shift.push(hash)
            u.is_confirmed = true
            u.save
        end
        data = {:kerbero => current_user.kerbero_id, :head_name => current_user.position, :request => shift}
        json = data.to_json
        
        uri = URI.parse("http://20.78.224.237:8000/api/register_rest_request/")
        http = Net::HTTP.new(uri.host, uri.port)
        http.use_ssl = false
        http.verify_mode = OpenSSL::SSL::VERIFY_NONE
    
        http.start do
          req = Net::HTTP::Post.new(uri.path)
          req.set_form_data(body: json)
          response = http.request(req)
        end
        render plain: {response.code => data}.to_json
    end

    private
    def set_kerberos
        @kerbero = Kerbero.find(session[:kerbero_id])
    end
end
