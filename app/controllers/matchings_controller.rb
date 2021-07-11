class MatchingsController < ApplicationController
    before_action :authenticate_kerberos, :set_kerberos

    def index
        if @kerbero.is_male 
            @keisho = "さん"
        else
            @keisho = "くん"
        end
        if params[:id].blank?
            @kerberos = Kerbero.where(is_male: !@kerbero.is_male, is_confirmed: true)
            @file_name = "index"
        else
            @kerbero1 = Kerbero.find_by(id: params[:id].to_i, is_confirmed: true)
            if @kerbero1
                @left_email = User.find(@kerbero1.left_user_id).email
                @center_email = User.find(@kerbero1.center_user_id).email
                @right_email = User.find(@kerbero1.right_user_id).email
                @file_name = "show"
                follow = Follow.find_by(from_kerbero_id: session[:kerbero_id], to_kerbero_id: params[:id])
                if follow
                    @is_followed = true
                else
                    @is_followed = false
                end
            else
                @kerberos = Kerbero.where(is_male: !@kerbero.is_male, is_confirmed: true)
                @file_name = "index"
            end
        end
    end

    def following
        if @kerbero.is_male 
            @keisho = "さん"
        else
            @keisho = "くん"
        end
        follows = Follow.where(from_kerbero_id: session[:kerbero_id])
        @kerberos = []
        follows.each do |f|
            kerbero = Kerbero.find_by(id: f.to_kerbero_id)
            if kerbero
                @kerberos.push(kerbero)
            end
        end
    end

    def follower
        if @kerbero.is_male 
            @keisho = "さん"
        else
            @keisho = "くん"
        end
        follows = Follow.where(to_kerbero_id: session[:kerbero_id])
        @kerberos = []
        follows.each do |f|
            kerbero = Kerbero.find_by(id: f.from_kerbero_id)
            if kerbero
                @kerberos.push(kerbero)
            end
        end
    end

    def follow
        if params[:id].blank?
            redirect_to kerberos_matching_path
        else
            follow = Follow.find_by(from_kerbero_id: session[:kerbero_id], to_kerbero_id: params[:id])
            if follow
                follow.destroy
            else
                follow = Follow.new
                follow.from_kerbero_id = session[:kerbero_id]
                follow.to_kerbero_id = params[:id]
                follow.save
                redirect_to kerberos_matching_path(:id => params[:id])
            end
        end
    end
    
    private
    def set_kerberos
        @kerbero = Kerbero.find(session[:kerbero_id])
    end

end
