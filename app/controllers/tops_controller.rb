class TopsController < ApplicationController
    def index
        if !session[:kerbero_id].blank?
            redirect_to kerberos_path
        end
    end
end
