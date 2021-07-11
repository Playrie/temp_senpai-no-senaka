class ApplicationController < ActionController::Base

    def after_sign_in_path_for(resource) 
        if current_user.is_set_id
            head_path
        else
            head_setting_path
        end
    end

    def after_sign_out_path_for(resource)
        if session[:kerbero_id]
            kerberos_path
        else
            root_path
        end
    end
    def authenticate_kerberos
        if session[:kerbero_id].blank?
            redirect_to kerberos_login_path
        else
            @kerbero = Kerbero.find(session[:kerbero_id])
            if !@kerbero.is_confirmed
                redirect_to kerberos_path
            end
        end
    end

    before_action :configure_permitted_parameters, if: :devise_controller?
    def configure_permitted_parameters
        devise_parameter_sanitizer.permit(:sign_up, keys: [:position,:kerbero_id])
        devise_parameter_sanitizer.permit(:account_update, keys: [:position,:kerbero_id])
    end
end
