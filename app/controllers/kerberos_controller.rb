class KerberosController < ApplicationController

    def new
        @kerbero = Kerbero.new
    end

    def create
        @kerbero = Kerbero.create(kerbero_params)
        if @kerbero.common_password == @kerbero.confirm_password
            session[:kerbero_id] = @kerbero.id
            case @kerbero.sex_num
            when 0
                @kerbero.is_male = true
                @kerbero.save
            when 1
                @kerbero.is_male = false
                @kerbero.save
            end
            redirect_to kerberos_path
        else
            @kerbero.delete
            redirect_to kerberos_signup_path
        end
    end

    def login
        if request.post?
            @kerbero = Kerbero.find_by(name: params[:name], common_password: params[:password])
            if @kerbero
                session[:kerbero_id] = @kerbero.id
                redirect_to kerberos_path
            else
                redirect_to kerberos_login_path
            end
        else
        end
    end

    def logout
        session[:kerbero_id] = nil
        redirect_to root_path
    end

    def index 
        if session[:kerbero_id]
            @kerbero = Kerbero.find(session[:kerbero_id])
        else
            redirect_to kerberos_login_path
        end
    end

    def edit
        if session[:kerbero_id]
            @kerbero = Kerbero.find(session[:kerbero_id])
        else
            redirect_to kerberos_login_path
        end
    end

    def update
        if session[:kerbero_id]
            @kerbero = Kerbero.find(session[:kerbero_id])
            if params[:old_password] == @kerbero.common_password && params[:common_password] == params[:confirm_password]
                @kerbero.name = params[:name]
                if !params[:confirm_password].blank?
                    @kerbero.common_password = params[:common_password]
                    @kerbero.confirm_password = params[:common_password]
                end
                @kerbero.age = params[:age]
                @kerbero.sex_num = params[:sex_num]
                case @kerbero.sex_num
                when 0
                    @kerbero.is_male = true
                when 1
                    @kerbero.is_male = false
                else
                    @kerbero.is_male = nil
                end
                @kerbero.save
                redirect_to kerberos_path
            end
        else
            redirect_to kerberos_login_path
        end
    end

    private
    def kerbero_params
        params.require(:kerbero).permit(:name, :common_password, :confirm_password, :sex_num)
    end

end
