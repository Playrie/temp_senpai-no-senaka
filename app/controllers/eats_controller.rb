class EatsController < ApplicationController
    def index
        
    end

    private
    def set_kerberos
        @kerbero = Kerbero.find(session[:kerbero_id])
    end
    
end
